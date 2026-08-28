## Description:

image-deck creates GPT Image 2 slide decks, PPT-style presentations, single slides, and carousel pages where each page is a complete generated raster image with visible text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tseng71](https://clawhub.ai/user/tseng71)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to plan, generate, review, revise, and optionally package image-based presentation decks when full-slide raster pages are acceptable. It is best suited for workflows that need consistent visual direction, visible text inside generated images, and explicit user approval before full deck generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated slide text, labels, or chart-like visuals may be inaccurate, missing, or hard to read.

Mitigation: Review each generated slide at full size and contact-sheet size, then regenerate slides with missing, incorrect, or unreadable content instead of patching text locally.

Risk: Users may expect an editable PowerPoint workflow, but this skill produces image-based slides.

Mitigation: Use this skill only when full-page raster slides are acceptable; choose a normal editable-presentation workflow for editable text, tables, or precise charts.

Risk: Generating the full deck before approval could lock in unwanted content or visual style.

Mitigation: Require overall design approval before generating one sample, then require separate approval of the displayed sample style before generating the remaining slides.

Risk: The skill depends on Codex built-in image_gen (GPT Image 2), which may not be available in every runtime.

Mitigation: Confirm the required image generation capability is available before use and stop or switch workflows if it is unavailable.

## Reference(s):

- [Prompt Patterns](references/prompt-patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/tseng71/skills/image-deck)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown planning text and prompt groups, optional helper commands or code, and generated image/PPTX/PDF files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces full-slide raster images with in-image text; optional PPTX/PDF assembly should preserve those images as the visible slide content.]

## Skill Version(s):

0.1.24 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
