#!/usr/bin/env python3
"""Regression tests for local/cloud judge selection."""

from __future__ import annotations

import importlib.util
import os
import sys
import types
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("run_eval.py")
SPEC = importlib.util.spec_from_file_location("rag_eval_under_test", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class FakeChatOllama:
    def __init__(self, model: str):
        self.model = model


class FakeHuggingFaceEmbeddings:
    def __init__(self, model_name: str):
        self.model_name = model_name


class FakeWrapper:
    def __init__(self, value):
        self.value = value


class SelectionTests(unittest.TestCase):
    def setUp(self):
        self.original_env = os.environ.copy()
        self.original_modules = dict(sys.modules)

        community = types.ModuleType("langchain_community")
        community.__path__ = []
        chat_models = types.ModuleType("langchain_community.chat_models")
        chat_models.ChatOllama = FakeChatOllama
        community.chat_models = chat_models

        ragas = types.ModuleType("ragas")
        ragas.__path__ = []
        ragas_llms = types.ModuleType("ragas.llms")
        ragas_llms.LangchainLLMWrapper = FakeWrapper
        ragas_embeddings = types.ModuleType("ragas.embeddings")
        ragas_embeddings.LangchainEmbeddingsWrapper = FakeWrapper

        huggingface = types.ModuleType("langchain_huggingface")
        huggingface.HuggingFaceEmbeddings = FakeHuggingFaceEmbeddings

        sys.modules.update({
            "langchain_community": community,
            "langchain_community.chat_models": chat_models,
            "ragas": ragas,
            "ragas.llms": ragas_llms,
            "ragas.embeddings": ragas_embeddings,
            "langchain_huggingface": huggingface,
        })

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self.original_env)
        sys.modules.clear()
        sys.modules.update(self.original_modules)

    def test_explicit_ollama_wins_over_cloud_keys(self):
        os.environ.update({
            "RAGAS_LLM": "ollama/local-model",
            "RAGAS_ALLOW_CLOUD": "1",
            "OPENAI_API_KEY": "test-openai-key",
            "ANTHROPIC_API_KEY": "test-anthropic-key",
        })
        wrapper = MODULE._get_llm()
        self.assertIsInstance(wrapper.value, FakeChatOllama)
        self.assertEqual(wrapper.value.model, "local-model")

    def test_explicit_ollama_forces_local_embeddings(self):
        os.environ.update({
            "RAGAS_LLM": "ollama/local-model",
            "RAGAS_ALLOW_CLOUD": "1",
            "OPENAI_API_KEY": "test-openai-key",
        })
        wrapper = MODULE._get_embeddings()
        self.assertIsInstance(wrapper.value, FakeHuggingFaceEmbeddings)
        self.assertEqual(wrapper.value.model_name, "BAAI/bge-small-en-v1.5")


if __name__ == "__main__":
    unittest.main()
