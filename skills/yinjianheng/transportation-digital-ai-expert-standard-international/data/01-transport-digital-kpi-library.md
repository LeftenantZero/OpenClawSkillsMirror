# Transport Digitalisation KPI Library (590+ KPIs)

> **Version**: V1.0.0 (International) | **Updated**: 2026-07-05 | **Total KPIs**: 570
> **Structure**: 15 transport modalities × 12 business chains × 10 KPI categories + 1 international benchmark extension
> **Sources**: Transport authorities, police/road-safety agencies, ITF, OECD, ISO/TC 204, USDOT/FHWA, European Commission (DG MOVE), LTA Singapore, TfL, ERTICO, ITS America, World Bank (LPI), ACI, and leading international city benchmarks (Singapore, Tokyo, London, Amsterdam, Seoul, New York)

---

## I. Transport Efficiency (85 KPIs)

### 1.1 Urban Road Traffic Efficiency

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 1 | average trip speed (km/h) | urban road network vehicle average travel speed | Σ( segment length × segment average speed )/Σ segment length | ≥38 | 28-35 | <22 | vehicle GP S/ mouth | 5 min | urban road |
| 2 | average Travel Time Index (TTI) (TTI) | actual travel time and free-flow travel time of ratio | TTI = actual travel time / free-flow travel time | ≤1.25 | 1.35-1.65 | ≥1.90 | vehicle / data | 15 min | urban road |
| 3 | congestion delay index | transport congestion caused by of additional time overhead multiple | during congestion time / during free-flow time | ≤1.31 | 1.50-1.80 | ≥2.00 | network platform | 15 min | urban road |
| 4 | network average saturation (V/C) | road segment actual flow and capacity ratio | V/C ratio = actual traffic volume / design capacity | ≤0.55 | 0.65-0.78 | ≥0.90 | line / / detect | 5 min | urban road / |
| 5 | share of congested distance (%) | severely congested segments distance share of total road network distance ratio | ( congested distance / total monitored network length )×100% | ≤5.0% | 8.0%-12.0% | ≥18.0% | vehicle / platform | 15 min | urban road |
| 6 | peak-hour volume share | peak hour traffic volume and all-day traffic volume ratio | ( peak hour traffic volume / all-day traffic volume )×100% | 6.5%-8.0% | 8.5%-10.0% | ≥12.0% | transport detect | h | urban road / |
| 7 | signalised intersection average delay (s/veh) | vehicle at signalised intersection of average waiting time | d = d1×PF + d2 + d3 (HCM ) | ≤35 | 45-65 | ≥85 | signal machine / electric data | cycle | urban road |
| 8 | green-wave coordination rate (%) | arterial road with green-wave coordination control of junctions share | ( green-wave coordination junctions count / signalised junctions total count )×100% | ≥65% | 35%-50% | ≤20% | signal control system | day | urban road |
| 9 | arterial travel-time volatility | arterial road day travel time standard deviation and mean ratio | CV = σ(T)/E[T] | ≤0.12 | 0.18-0.25 | ≥0.35 | vehicle data | day | urban road |
| 10 | bus lane traffic efficiency | bus lane utilisation composite indicator | ( bus operating speed / general traffic speed )× bus mode share | ≥1.20 | 0.85-1.05 | ≤0.65 | bus GP S+ vehicle | day | bus / urban road |
| 11 | reversible / dynamic lane utilisation rate (%) | reversible / dynamic lane actual utilisation | ( reversible / dynamic lane traffic volume / design capacity )/( full-section traffic volume / design capacity ) | ≥1.15 | 0.90-1.05 | ≤0.70 | line / detect | day | urban road |
| 12 | tidal-traffic balance index | PM peak directional imbalance coefficient -isation degree | ΔK = |K AM peak -K PM peak | | ≤0.15 | 0.25-0.35 | ≥0.50 | vehicle / detect | day | urban road |
| 13 | expressway / arterial on-ramp control effectiveness | ramp control before after mainline speed improve rate | ( control after speed - control before speed )/ control before speed ×100% | ≥25% | 12%-20% | ≤5% | / detect | day | / expressway / arterial |
| 14 | road segment travel-time predictability | travel time prediction error rate | MAPE = (Σ|T actual -T predict |/T actual )/n×100% | ≤8% | 12%-18% | ≥25% | predict system + measure | day | urban road / |
| 15 | network connectivity index | road network in each inter-node connectivity | J = (ΣL/ξ)/(A×N)^0.5 | ≥2.5 | 1.8-2.3 | ≤1.4 | road network GIS data | month | urban road |
| 16 | road network road-class hierarchy rationality | expressway / arterial : arterial road : secondary road : local road degree ratio | each road degree share deviation from national-standard recommended values | deviation ≤10% | deviation 10%-25% | deviation ≥40% | road network GIS data | year | urban road |
| 17 | vehicle effectiveness rate (%) | information guide vehicle to vehicle of rate | ( vehicle count / total time count )×100% | ≥85% | 70%-80% | ≤55% | vehicle system | day | urban road / vehicle |
| 18 | transport event detect time (min) | from from incident occurrence to detected by the system average time | TTD = T detect -T occur | ≤2 | 4-8 | ≥15 | event detect system | real-time | urban road / |
| 19 | event response time (min) | from detect event to response unit arrival of average time | TTR = T arrival -T detect | ≤8 | 12-20 | ≥35 | refers to dispatch system | real-time | urban road / |
| 20 | event clear time (min) | from from incident occurrence to return to normal traffic of total time | TTC = T clear -T occur | ≤15 | 25-45 | ≥90 | refers to dispatch system | event | urban road / |
| 21 | work zone transport organise efficiency | work zone area actual capacity retention rate | ( during construction capacity / original capacity )×100% | ≥75% | 55%-68% | ≤40% | construction manage system | day | urban road / |
| 22 | road line ensure effectiveness rate (%) | special duty road line ensure rate | ( successful assurance count / total assurance count )×100% | ≥99.5% | 97%-99% | ≤95% | refers to dispatch system | event | urban road |
| 23 | traffic situation prediction accuracy (%) | AI predict of transport status and actual of consistency | ( correctly predicted time steps / total time steps )×100% | ≥95% | 85%-92% | ≤75% | AI predict + measure | day | urban road |
| 24 | tidal lane time to take effect (min) | tidal lane from switch to stable operation of time | T stable -T switch start | ≤3 | 5-8 | ≥15 | signal control system | switch | urban road |
| 25 | micro-circulation network utilisation rate (%) | local road and internal roads traffic diversion share | ( micro-circulation road flow / zone total flow )×100% | ≥20% | 12%-16% | ≤6% | vehicle + detect | month | urban road |

### 1.2 Expressway Efficiency

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 26 | expressway average travel speed (km/h) | road network vehicle average travel speed | Σ( segment length × average speed )/Σ segment length | ≥100 | 85-98 | ≤68 | ETC / data | 5 min | expressway |
| 27 | expressway saturation (V/C) (V/C) | expressway road segment actual flow and capacity ratio | V/C = actual traffic volume (Q)/ design capacity (C) | ≤0.45 | 0.55-0.68 | ≥0.85 | ETC / detect | 5 min | expressway |
| 28 | expressway during congestion (h/d) | daily in congested state ( speed <40km/h) of cumulative hr | Σ(T congestion )/ day | ≤0.5 | 1.5-3.0 | ≥6.0 | ETC data | day | expressway |
| 29 | expressway congested distance ratio (%) | congested distance share of total monitor distance of share | ( congested distance / total distance )×100% | ≤0.5% | 1.0%-2.5% | ≥5.0% | ETC / data | day | expressway |
| 30 | ETC lane pass-through rate (%) | ETC lane vehicle first-pass rate | ( single-pass vehicle count /ETC total vehicle time )×100% | ≥99.5% | 98.0%-99.2% | ≤96.5% | ETC system | day | expressway |
| 31 | ETC transaction success rate (%) | ETC electric transaction complete rate | ( transaction count / total transaction count )×100% | ≥99.9% | 99.5%-99.8% | ≤99.0% | ETC compute system | day | expressway |
| 32 | station average service time (s) | vehicle at lane of average dwell time | MTC lane ≤8s,ETC lane ≤0.6s | ≤5(MTC) | 8-12(MTC) | ≥18(MTC) | system | day | expressway |
| 33 | station team degree (m) | toll plaza vehicle average queue length | peak period per lane team degree mean | ≤20 | 35-60 | ≥120 | / detect | 15 min | expressway |
| 34 | service district saturation (V/C) (%) | service district vehicle use rate | ( occupied spaces / total spaces )×100% | ≤60% | 72%-85% | ≥95% | service district manage system | day | expressway |
| 35 | service district average stopping time (min) | vehicle at service district within average hr | Σ( field time - field time )/ vehicle count | ≤15 | 20-30 | ≥45 | service district mouth system | day | expressway |
| 36 | truck share over-limit segment share (%) | truck share exceed design value of road segment distance ratio | ( freight wagon over-limit segment distance / total distance )×100% | ≤3% | 5%-10% | ≥18% | ETC vehicle-class recognition | month | expressway |
| 37 | construction segment traffic efficiency retention rate (%) | work zone actual capacity and design capacity ratio | ( actual volume / work zone design capacity )×100% | ≥80% | 60%-72% | ≤42% | ETC data | day | expressway |
| 38 | road network travel-time reliability | travel time 95th percentile value and mean ratio | buffer index = (T95-Tmean)/Tmean | ≤0.15 | 0.22-0.35 | ≥0.55 | ETC / | day | expressway |
| 39 | hub interchange transfer efficiency | interchange ramp time and mainline time ratio | T ramp /(L ramp /V mainline ) | ≤1.3 | 1.5-1.9 | ≥2.8 | ETC data | day | expressway |
| 40 | expressway license plate recognition accuracy (%) | ETC license plate automatic recognition accuracy | ( identify count / total count )×100% | ≥99.5% | 98.0%-99.2% | ≤96.0% | ETC system | day | expressway |

### 1.3 Public Transport Efficiency

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 41 | average bus operating speed (km/h) | bus vehicle at on the operating route average travel speed （ including stops ） | route distance / total operating time | ≥22 | 16-20 | ≤12 | bus GP S system | day | public bus |
| 42 | bus on-time arrival rate (%) | bus vehicle per schedule operate of punctuality (on-time) rate | ( on-time arrival vehicle time / total operation vehicle time )×100% | ≥92% | 80%-88% | ≤68% | bus dispatch system | day | public bus |
| 43 | bus headway deviation rate (%) | actual headway and planned headway of deviation degree | |T actual -T plan |/T plan ×100% | ≤8% | 12%-18% | ≥30% | bus dispatch system | day | public bus |
| 44 | bus average transfer time (min) | passenger at not bus line road of average transfer waiting time | Σ( boarding stop time - alighting stop time )/ number of transfers | ≤5 | 8-12 | ≥20 | IC / GP S data | day | public bus |
| 45 | bus network density (km/km²) | city built-up area per-unit area bus line road degree | bus line road total degree / built-up area | ≥4.0 | 2.8-3.5 | ≤1.8 | bus line network GIS | year | public bus |
| 46 | bus 500 m stop coverage (%) | built-up area bus stop / station 500 m radius share of covered area | (500m covered area / built-up area total area )×100% | ≥95% | 80%-90% | ≤65% | bus line network GIS | year | public bus |
| 47 | rail transit punctuality (on-time) rate (%) | rail transit train timetable on-time operation share | ( point train count / total operated trips )×100% | ≥99.9% | 99.5%-99.8% | ≤99.0% | rail transit dispatch system | day | rail transit |
| 48 | rail transit timetable timetable fulfilment rate (%) | actual operated trips and plan operated trips ratio | ( actual operated trips / plan operated trips )×100% | ≥99.9% | 99.5%-99.8% | ≤98.5% | rail transit dispatch system | day | rail transit |
| 49 | rail transit peak load factor (%) | rail transit carriage peak period standing density or degree | ( peak segment passenger flow / train capacity )×100% | ≤85% | 95%-110% | ≥130% | AFC system | day | rail transit |
| 50 | rail transit minimum headway (s) | rail transit line road minimum tracking headway | line road signalling system minimum design headway | ≤90 | 110-150 | ≥240 | signalling system | month | rail transit |
| 51 | rail transit transfer station average transfer time (s) | passenger at between rail lines transfer of average walking + waiting time | transfer road time + average waiting time | ≤180 | 220-300 | ≥420 | AFC+ positioning | month | rail transit |
| 52 | BRT system operating speed (km/h) | BRT system vehicle average operating speed | BRT line road degree / operation time | ≥25 | 18-24 | ≤13 | BRT dispatch system | day | BRT |
| 53 | BRT station throughput ( persons/h ) | BRT station maximum hourly passenger throughput | one-way hourly passenger throughput | ≥12000 | 6000-9000 | ≤3500 | AFC data | day | BRT |

### 1.4 Integrated Transport Hub Efficiency

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 54 | hub average transfer time (min) | passenger at integrated hub between modes transfer of average time | Σ( transfer walking + waiting time )/ transfer trips | ≤8 | 12-18 | ≥30 | hub passenger-flow monitoring system | day | composite hub |
| 55 | hub passenger dispersal time (min) | large-scale passenger from hub arrival to departure of average time | exit time - arrival time （ statistical mean ） | ≤15 | 22-32 | ≥50 | hub passenger-flow monitoring system | day | composite hub |
| 56 | hub transfer walking distance (m) | between modes transfer of average | Σ transfer walking distance / transfer trips | ≤200 | 280-400 | ≥650 | hub GIS/ positioning | month | composite hub |
| 57 | hub security screening throughput (persons/h) | hub security lane time via person count | security screening via trips / h | ≥500 | 350-420 | ≤220 | security screening machine system | day | composite hub |
| 58 | hub signage guidance effectiveness (%) | passenger relying on signage successfully locating destination of share | ( persons who found destination / surveyed persons )×100% | ≥95% | 85%-92% | ≤72% | user + analyse | quarter | composite hub |

### 1.5 Port & Waterway Efficiency

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 59 | port throughput ( 10k TEU /year ) | port annual container TEU process total volume | Σ per berth annual container volume | ≥3000 | 800-2000 | ≤300 | port manage system | month | port & waterway |
| 60 | vessel average time-in-port (h) | vessel from arrival departure average dwell time | Σ( departure time - arrival time )/ vessel count | ≤12 | 18-28 | ≥48 | AIS/ port dispatch system | day | port & waterway |
| 61 | container quayside handling efficiency ( TEU /h) | unit quay crane h TEU volume | number of containers handled / working time | ≥45 | 28-38 | ≤18 | TOS system | shift time | port & waterway |
| 62 | container yard turnaround day count ( day ) | container at container yard average storage days | Σ( field day - field day )/ volume | ≤3 | 5-8 | ≥14 | TOS system | month | port & waterway |
| 63 | port collecting & distributing efficiency (%) | drayage truck from entering port to leaving port 2 h within complete share | (2h within complete collecting & distributing vehicle time / total vehicle time )×100% | ≥90% | 72%-83% | ≤55% | drayage truck dispatch system | day | port & waterway |
| 64 | foreign-trade vessel direct-berthing rate (%) | foreign-trade vessel direct berthing on arrival （ without waiting for berth ） share | ( berthing vessel count / total arriving vessels )×100% | ≥75% | 55%-68% | ≤35% | port dispatch system | month | port & waterway |
| 65 | port customs clearance paperless rate (%) | customs documents electronic processing share | ( electronic documents count / total documents count )×100% | ≥98% | 85%-95% | ≤65% | Single Window system | month | port & waterway |

### 1.6 Civil Aviation Efficiency

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 66 | flight on-time rate (%) | flight at scheduled time within ±15 minutes within departure / arrival of share | ( on-time flight count / operated flights total count )×100% | ≥85% | 75%-82% | ≤65% | civil aviation operate system | day | civil aviation |
| 67 | machine field average taxi time (min) | aircraft taxiing from stand to runway （ or vice versa ） of average time | Σ( take-off time - pushback time )/ flight count | ≤12 | 16-22 | ≥35 | ADS-B/ surface surveillance | day | civil aviation |
| 68 | machine field average delay (min) | flight mean deviation from schedule | Σ(| actual time - scheduled time |)/ flight count | ≤15 | 22-35 | ≥55 | civil aviation operate system | day | civil aviation |
| 69 | machine field capacity utilisation (%) | machine field h actual take-off & landing movements and volume on ratio | ( actual take-off & landing movements / approved capacity )×100% | ≤80% | 85%-92% | ≥100% | ATC operate data | day | civil aviation |
| 70 | airspace utilisation rate (%) | available airspace sectors actual utilisation | ( actual flight volume / airspace volume )×100% | 65%-78% | 78%-88% | ≥95% | ATC automation system | day | civil aviation |
| 71 | passenger security screening throughput (persons/h) | passengers screened per hour per lane | security screening via trips / h | ≥200 | 150-180 | ≤100 | security screening information system | day | civil aviation |
| 72 | baggage mishandling rate (‰) | per 1,000 bags in occur mishandled pieces | ( mishandling baggage count / total baggage count )×1000‰ | ≤0.5‰ | 1.5‰-3.0‰ | ≥6.0‰ | baggage process system | day | civil aviation |
| 73 | air-cargo terminal process efficiency ( tonnes/day ) | air-cargo terminal daily average freight process volume | daily cargo & mail handled | ≥800 | 400-600 | ≤180 | freight transport station manage system | day | civil aviation |
| 74 | machine field surface-access connection time (min) | average surface access time from city centre to airport | Σ( arrival passenger surface transport time )/ passenger count | ≤35 | 45-65 | ≥90 | / taxi data | month | civil aviation / urban traffic |

### 1.7 Railway Efficiency

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 75 | railway train punctuality (on-time) rate (%) | passenger trains per timetable on-time operation share | ( point train count / total train count )×100% | ≥99.0% | 96%-98.5% | ≤93% | railway dispatch system | day | railway |
| 76 | HSR average operating speed (km/h) | HSR train average travel speed | operating mileage / operation time | ≥280 | 240-270 | ≤200 | railway dispatch system | day | HSR |
| 77 | railway marshalling yard classification capability ( vehicle / day ) | marshalling yard daily average classification freight wagon count volume | average wagons classified per day | ≥8000 | 4500-6500 | ≤2500 | marshalling yard manage system | day | railway freight transport |
| 78 | railway container terminal as efficiency ( TEU /h) | railway container yard h capability | number of containers handled / working time | ≥35 | 22-28 | ≤12 | railway container system | day | railway freight transport |
| 79 | railway freight transport vehicle week time ( day ) | wagon from one loading to next of average | Σ( time between re-loading and current loading )/ vehicle count | ≤2.5 | 3.2-4.5 | ≥7.0 | railway freight wagon manage system | day | railway freight transport |

### 1.8 Active Transportation Efficiency

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 80 | bike-share turnover rate ( time / vehicle · day ) | per vehicle bike-share daily average use time count | daily bike trips / deployed fleet size | ≥4.5 | 2.5-3.5 | ≤1.2 | bike-share platform | day | shared mobility |
| 81 | bike-share hotspot area dispatch efficiency (min) | from imbalance detection to dispatch recovery of average time | T recover -T detect | ≤30 | 45-80 | ≥120 | bike-share O&M system | day | shared mobility |
| 82 | walkability index | residents within 15-min walk daily-life POIs of share | ( accessible facility types in living circle /8)×100% | ≥90% | 70%-82% | ≤50% | POI+ road | year | active transportation |
| 83 | bike lane continuity (%) | continuous bike-lane segments share of bike lane total distance ratio | ( road segment distance / bike lane total distance )×100% | ≥85% | 65%-78% | ≤40% | road GIS | year | active transportation |
| 84 | bike lane shade coverage (%) | bike lane both sides shaded mileage share | ( has distance / bike lane total distance )×100% | ≥70% | 45%-60% | ≤25% | roadside remote sensing / street view | year | active transportation |
| 85 | e-bike charging efficiency | average public charging duration | Σ charging duration / charging sessions | ≤180min | 210-260min | ≥360min | electric platform | day | active transportation |

---

## II. Transport Safety (68 KPIs)

### 2.1 Road Traffic Crash Metrics

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 86 | fatalities per 10k vehicles ( person / vehicle ) | annual traffic fatalities per 10k motor vehicles | ( year traffic crash fatalities / vehicle fleet ( vehicle )) | ≤1.0 | 2.5-4.5 | ≥7.0 | manage crash count | year | urban road / |
| 87 | fatalities per 100k population ( person /10 per 10k persons ) | annual traffic fatalities per 100k residents | ( year traffic crash fatalities / resident population (10 )) | ≤2.0 | 3.5-5.5 | ≥8.5 | manage crash count | year | road |
| 88 | fatalities per 100M veh-km ( person / per 100M veh-km ) | traffic fatalities per 100M veh-km | ( year crash fatalities / year veh-km ( )) | ≤0.5 | 0.8-1.5 | ≥3.0 | manage crash count + vehicle | year | road |
| 89 | traffic crash incident rate ( per million veh-km ) | traffic crashes per million veh-km | ( crash count / veh-km ( )) | ≤0.8 | 1.2-2.0 | ≥4.0 | manage crash count | month | road |
| 90 | expressway crash rate ( per 100M veh-km ) | expressway per 100M veh-km crash count | ( expressway crashes / veh-km ( )) | ≤15 | 25-45 | ≥80 | manage crash count | month | expressway |
| 91 | traffic crash serious-injury rate (%) | serious injuries as share of total casualties | ( serious injury person count /( + serious injury + minor injury total person count ))×100% | ≤10% | 15%-22% | ≥30% | manage crash count | year | road |
| 92 | traffic crash property-damage rate ( $ per 10k veh-km ) | direct property damage per 10k veh-km | crash direct property loss / veh-km | ≤50 | 80-150 | ≥350 | manage crash count | month | road |
| 93 | crash black-spot treatment rate (%) | treated black spots as share of identified | ( treated black spot count / identified black spots total count )×100% | ≥90% | 65%-80% | ≤40% | safety management system | year | road |
| 94 | crash black spot governance effectiveness rate (%) | post-treatment crash-rate reduction | ( governance before crash rate - post-treatment crash rate )/ governance before ×100% | ≥65% | 35%-52% | ≤15% | crash for ratio analyse | year | road |
| 95 | e-bike crash share (%) | e-bike-involved crashes as share | ( electric crash count / total crash count )×100% | ≤8% | 12%-20% | ≥32% | manage crash count | month | urban road |

### 2.2 Active Safety & Early-Warning Metrics

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 96 | risk early-warning coverage (%) | transport risk point covered by intelligent early-warning | ( covered risk points / total identified risk points )×100% | ≥85% | 55%-72% | ≤25% | transport safety system | month | road |
| 97 | warning accuracy (%) | true-positive warning rate | ( warning count / total warning count )×100% | ≥92% | 78%-88% | ≤60% | safety early-warning system | day | road |
| 98 | warning timeliness (s) | avg time from risk occurrence to warning push | T push -T risk occurrence | ≤1.0 | 2.5-5.0 | ≥12.0 | safety early-warning system | real-time | road |
| 99 | secondary-crash prevention effectiveness rate (%) | secondary-crash reduction via warning | ( after secondary-crash reduction ) | ≥75% | 45%-65% | ≤20% | crash count for ratio | month | / expressway / arterial |
| 100 | adverse weather safety warning accuracy (%) | adverse-weather warning accuracy | ( day warning count / total weather events )×100% | ≥90% | 75%-85% | ≤58% | + transport convergence system | day | road / / waterway |
| 101 | V2X safety message rate (%) | V2X safety message ( BSM / RSM etc.) rate | ( successfully received messages / transmitted messages )×100% | ≥99.9% | 98.5%-99.5% | ≤95.0% | V2X communications measure test platform | day | V2X |
| 102 | V2X safety message latency (ms) | end-to-end latency of safety messages | T receive -T transmit | ≤10 | 20-50 | ≥100 | V2X communications measure test platform | s | V2X |
| 103 | tunnel safety monitoring coverage rate (%) | tunnel safety-monitoring coverage | ( instrumented tunnel length / total tunnel length )×100% | ≥95% | 80%-90% | ≤60% | road manage system | month | expressway |
| 104 | bridge health monitoring coverage rate (%) | key-bridge health-monitoring coverage | ( instrumented bridges / total key bridges )×100% | ≥85% | 55%-72% | ≤30% | manage system | year | road / city |
| 105 | transport electronic-enforcement rate (%) | off-site enforcement share of total violations | ( off-site enforcement count / total enforcement )×100% | ≥70% | 45%-60% | ≤25% | transport enforcement system | month | road |

### 2.3 Rail Transit / Bus Safety Metrics

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 106 | rail transit delay over 5 minutes event rate ( / per million veh-km ) | 5-min+ delays per million train-km | (5min+ delay incident count / veh-km ( )) | ≤0.15 | 0.30-0.55 | ≥1.20 | rail operation manage system | month | rail transit |
| 107 | rail transit passenger casualty rate ( person / 100 million passenger-trips ) | passenger casualties per 100M trips | ( passenger casualties / passenger volume (100M) ) | ≤0.01 | 0.03-0.08 | ≥0.25 | rail operation manage system | year | rail transit |
| 108 | bus crash rate ( / km) | bus crashes per million operating km | ( total crashes / total operating distance ( km)) | ≤0.8 | 1.2-2.0 | ≥4.0 | bus safety management | month | public bus |
| 109 | bus driver fatigue driving warning effectiveness rate (%) | driver-fatigue detection accuracy | ( correct fatigue warnings / total fatigue warnings )×100% | ≥88% | 72%-82% | ≤55% | in-vehicle DSM system | day | bus / freight transport |
| 110 | rail transit signalling system failure rate ( time / train-km ) | signalling failures per 10k train-km | ( signalling failures / train-km ( )) | ≤0.05 | 0.12-0.25 | ≥0.60 | signal maintain system | month | rail transit |

### 2.4 Waterway / Aviation Safety Metrics

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 111 | marine casualty rate ( / per 10k vessel calls ) | marine casualties per 10k vessel calls | ( crash count / vessel port calls ( )) | ≤0.5 | 1.0-2.0 | ≥5.0 | manage system | month | waterway |
| 112 | port work safety crash rate ( / 100M tonnes ) | work-safety incidents per 100M tonnes throughput | ( work-safety incidents / cargo throughput (100M tonnes) ) | ≤0.3 | 0.6-1.2 | ≥3.0 | port safety management system | month | port |
| 113 | VTS -covered waters crash rate ( / per 10k vessel calls ) | crash rate in VTS -covered waters | crashes in VTS area / per 10k vessel calls | ≤0.3 | 0.6-1.0 | ≥2.5 | VTS + data | month | waterway |
| 114 | aviation safety serious incident rate ( / per 10k movements ) | serious incidents per 10k movements | ( serious incidents / flight movements (10k) ) | ≤0.02 | 0.05-0.12 | ≥0.35 | aviation safety manage | month | civil aviation |
| 115 | runway incursion event rate ( / per 10k movements ) | runway incursions per 10k movements | ( runway incursions / movements (10k) ) | ≤0.15 | 0.30-0.55 | ≥1.20 | surface surveillance / ATC | month | civil aviation |
| 116 | FOD damage event rate ( / per 1k movements ) | FOD damages per 1k movements | ( FOD damage events / flight movements (1k) ) | ≤0.02 | 0.05-0.10 | ≥0.30 | machine field safety management | month | civil aviation |

### 2.5 Cybersecurity & Data Security

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 117 | transport system annual cybersecurity incidents | annual security incidents of transport IT systems | total annual cybersecurity incidents | 0 | 2-5 | ≥15 | safety manage in / situation sensing | month | complete |
| 118 | vulnerability remediation average time (h) | avg time from high-risk vuln discovery to full patch | T patch completed -T vuln discovery | ≤4 | 12-24 | ≥72 | manage platform | day | complete |
| 119 | security incident response time (min) | avg time from detection to response | T response launched -T event detection | ≤5 | 15-30 | ≥60 | SOC/ safety manage platform | real-time | complete |
| 120 | data backup & recovery rate (%) | critical-data successful recovery within SLA | ( successful recoveries / total recovery tests )×100% | ≥99.9% | 98.0%-99.5% | ≤95.0% | system | month | complete |
| 121 | data encryption coverage rate (%) | encrypted data share in transit & at rest | ( encrypted volume / total volume )×100% | ≥98% | 80%-92% | ≤55% | data safety assess | quarter | complete |
| 122 | personal information compliance level (%) | personal-info compliance pass rate | ( passed checks / total checks )×100% | ≥98% | 85%-95% | ≤68% | assess system | quarter | complete |
| 123 | etc. compliance rate (%) | information system via etc. measure of share | ( via etc. measure system count / should measure system total count )×100% | 100% | 85%-98% | ≤60% | etc. measure | year | complete |
| 124 | safety situation sensing coverage rate (%) | by safety situation sensing system of IT share | ( by count / total IT count )×100% | ≥95% | 70%-85% | ≤40% | safety situation sensing platform | month | complete |

### 2.6 Road Infrastructure Safety

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 125 | road line rate (%) | transport line of road share | ( line road / road total )×100% | ≥95% | 82%-90% | ≤65% | manage system / inspection tour | month | road |
| 126 | road compliance rate (%) | degree and degree meet standard of road share | ( compliant road / road total )×100% | ≥92% | 78%-88% | ≤58% | manage system | month | road |
| 127 | etc. compliance rate (%) | etc. design standard of road segment share | ( compliant degree / total degree )×100% | ≥95% | 82%-90% | ≤65% | manage system | year | road |
| 128 | road surface property can rate (%) | road surface count ( or SFC) compliant road segment share | ( property can compliant road / detect road total )×100% | ≥90% | 78%-86% | ≤60% | road surface detect vehicle | year | road |
| 129 | road safety hazard rate (%) | screening of safety hazard complete of share | ( hazard count / screening hazard total count )×100% | ≥92% | 72%-85% | ≤48% | safety hazard manage system | month | road |
| 130 | under warning facility coverage rate (%) | under road segment safety early-warning facility installed rate | ( installed warning facility under count / under road segment total count )×100% | ≥80% | 55%-68% | ≤25% | safety facility manage system | year | / country province road |

### 2.7 Driver & Behavioural Safety

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 131 | point vehicle supervision coverage rate (%) | " passenger " vehicle supervision platform of share | ( network supervision vehicle count / should supervision vehicle total count )×100% | ≥99% | 90%-97% | ≤75% | point vehicle supervision platform | month | road |
| 132 | point vehicle exceeding rate ( time / vehicle · day ) | vehicle point vehicle daily average exceeding time count | ( exceeding total count / network vehicle count ( ))×100% | ≤0.5 | 2.0-5.0 | ≥15.0 | point vehicle platform | day | road |
| 133 | for risk assess coverage rate (%) | for safety assess of transport driver share | ( assess driver count / transport driver total count )×100% | ≥80% | 45%-65% | ≤20% | for analyse platform | month | road / bus / freight transport |
| 134 | freight transport vehicle fatigue driving share (%) | fatigue driving and of vehicle share of total operation vehicle of share | ( occur fatigue driving vehicle count / total deployed fleet size )×100% | ≤3% | 6%-10% | ≥20% | freight transport supervision platform | day | freight transport |
| 135 | -isation transport electric transport coverage rate (%) | -isation transport use electric transport manage of share | ( electric transport transport time count / total transport time count )×100% | ≥98% | 75%-90% | ≤45% | -isation transport supervision platform | month | freight transport / -isation |

---

## III. Infrastructure (76 KPIs)

### 3.1 Highway Infrastructure

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 136 | road network density (km/ km²) | km country earth area within of road distance | ( road total distance / country earth area ( km²)) | ≥150 | 80-120 | ≤25 | transport transport count year | year | road |
| 137 | expressway density (km/ km²) | km country earth area within of expressway distance | ( expressway distance / country earth area ( km²)) | ≥5.0 | 2.0-3.8 | ≤0.8 | transport transport count year | year | |
| 138 | road road surface technology index (PQI) | road surface use property can composite index | PQI=w1PCI+w2RQI+w3RDI+w4SRI | ≥92 | 85-90 | ≤75 | road surface detect / system | quarter | road |
| 139 | road technology etc. Ⅰ type share (%) | technology for Ⅰ type of share | (Ⅰ type count / total count )×100% | ≥70% | 55%-65% | ≤35% | manage system (CBMS) | year | road |
| 140 | road road technology etc. Ⅰ type share (%) | technology for Ⅰ type of road share | (Ⅰ type road count / road total count )×100% | ≥65% | 48%-60% | ≤30% | road manage system | year | road |
| 141 | road funding intensity ( $10k /km) | road distance annual | year total / road total distance | ≥12 | 6.5-9.5 | ≤3.0 | manage system | year | road |
| 142 | expressway video surveillance coverage rate (%) | expressway line video surveillance point cover share | ( cover segment length / total distance )×100% | ≥95% | 80%-90% | ≤60% | video surveillance system | year | expressway |
| 143 | expressway ETC coverage rate ( for /100km) | expressway km average ETC for count | ETC total for count /( distance /100) | ≥4.0 | 2.8-3.5 | ≤1.5 | ETC system | year | expressway |
| 144 | country province road road rate (%) | country province road in technology road segment share | ( road distance / country province road total distance )×100% | ≥88% | 78%-85% | ≤65% | road count | year | country province road |
| 145 | agriculture village road in etc. road rate (%) | agriculture village road in technology in etc. road segment share | ( in etc. road distance / agriculture village road total distance )×100% | ≥85% | 72%-80% | ≤55% | road count | year | agriculture village road |
| 146 | highway infrastructure digital -isation rate (%) | highway infrastructure with digital -isation manage of share | ( digital -isation item count / should digital -isation item count )×100% | ≥85% | 45%-68% | ≤18% | asset management system | year | road |

### 3.2 Traffic Sensing & Information Infrastructure

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 147 | urban traffic sensing equipment density ( unit /km) | urban road km average transport sensing equipment count volume | Σ( each sensing equipment total count )/ urban road total distance | ≥25 | 12-20 | ≤4 | equipment manage system | year | urban road |
| 148 | expressway sensing equipment density ( unit /km) | expressway km average sensing equipment count | Σ sensing equipment count / total distance | ≥8 | 3.5-6.0 | ≤1.2 | equipment manage system | year | expressway |
| 149 | sensing equipment online rate (%) | sensing equipment operate online of share | ( online equipment count / equipment total count )×100% | ≥99% | 95%-98% | ≤88% | equipment O&M platform | day | complete |
| 150 | sensing data rate (%) | sensing equipment actual collect data volume and collect data volume ratio | ( actual data item count / data item count )×100% | ≥98% | 90%-96% | ≤75% | data quality platform | day | complete |
| 151 | quality compliance rate (%) | video surveillance quality meet GA/T standard need of share | ( quality compliant machine count / total count )×100% | ≥95% | 82%-92% | ≤65% | O&M platform | month | road |
| 152 | V2X RSU coverage rate ( unit /100km²) | city built-up area km RSU count volume | RSU total count /( built-up area /100) | ≥300 | 100-220 | ≤20 | V2X manage platform | year | V2X |
| 153 | 5G-V2X network coverage rate (%) | urban road 5G-V2X communications network cover share | (5G-V2X cover road / urban road total )×100% | ≥85% | 35%-60% | ≤10% | communications manage system | year | V2X |
| 154 | high-precision positioning cover can use property (%) | high-precision positioning (GNSS+RTK) service can use time share | ( positioning can use hr / total operation hr )×100% | ≥99.9% | 98.0%-99.5% | ≤95.0% | high-precision positioning platform | day | complete |
| 155 | edge calculate node density ( unit /100km²) | city built-up area km edge calculate node count | edge node total count /( built-up area /100) | ≥50 | 15-35 | ≤3 | edge calculate manage platform | year | urban road |

### 3.3 Rail / Port / Airport Infrastructure

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 156 | rail transit operating mileage (km) | city rail transit operation of line road total degree | Σ each line road operating mileage | ≥600 | 200-450 | ≤50 | rail transit count | year | rail transit |
| 157 | rail transit vehicle station count ( ) | city rail transit operation vehicle station total count | Σ each line vehicle station count ( not plan transfer station ) | ≥300 | 100-250 | ≤25 | rail transit count | year | rail transit |
| 158 | rail transit complete autonomous driving line road share (%) | use GOA4 complete autonomous driving line road distance share | (GoA4 line road distance / total operating mileage )×100% | ≥25% | 8%-18% | ≤2% | rail transit count | year | rail transit |
| 159 | rail transit network density (km/km²) | built-up area per-unit area rail transit line road degree | ( rail transit operating mileage / built-up area ) | ≥0.6 | 0.25-0.45 | ≤0.08 | rail transit count | year | rail transit |
| 160 | port 10k tonnes with on berth count ( unit ) | port 10k tonnes and with on water berth total count | 10k tonnes and with on berth count volume | ≥350 | 80-200 | ≤15 | port count year | year | port |
| 161 | port design throughput ( 100M tonnes / year ) | port year design freight throughput | Σ per berth design throughput | ≥5.0 | 1.5-3.5 | ≤0.3 | port count year | year | port |
| 162 | port automatic -isation share (%) | automatic -isation container berth count volume share | ( automatic -isation berth count / container berth total count )×100% | ≥15% | 3%-8% | ≤0.5% | port count | year | port |
| 163 | machine field passenger throughput ( per 10k persons time / year ) | machine field year passenger leaving port total trips | year leaving port passenger total volume | ≥5000 | 1200-3500 | ≤200 | civil aviation count | month | civil aviation |
| 164 | machine field freight postal throughput ( 10k tonnes / year ) | machine field year freight postal leaving port total volume | year leaving port cargo & mail volume | ≥200 | 25-120 | ≤3 | civil aviation count | month | civil aviation |
| 165 | machine field A-CDM system coverage rate (%) | machine field implement coordination (A-CDM) system of share | ( has A-CDM machine field count / year machine field count )×100% | 100% | 60%-85% | ≤30% | civil aviation operate count | year | civil aviation |
| 166 | railway electric -isation rate (%) | electric -isation railway distance share of railway distance of share | ( electric -isation distance / railway distance )×100% | ≥75% | 60%-72% | ≤40% | railway count | year | railway |

### 3.4 Intelligent Infrastructure & Systems

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 167 | urban traffic signal network rate (%) | signal control platform of junctions share | ( network signal junctions count / signal junctions total count )×100% | ≥90% | 55%-75% | ≤18% | signal control system | quarter | urban road |
| 168 | city intelligent transport manage platform / composite traffic operation in rate (%) | with on city traffic operation in of share | ( has composite traffic operation in number of cities / with on city total count )×100% | ≥60% | 25%-42% | ≤8% | transport transport count | year | urban traffic |
| 169 | can / information cover density ( /10km) | urban road 10 km can information publish count volume | information total count /( urban road distance /10) | ≥8 | 3-6 | ≤0.5 | information publish system | year | urban road / |
| 170 | roadside intelligent station density ( unit /10km) | urban road 10 km can smart / intelligent station count | intelligent station count /( road degree /10) | ≥15 | 5-10 | ≤1 | intelligent manage system | year | urban road |
| 171 | electric coverage rate ( unit / vehicle EV) | vehicle electric vehicle corresponding of public charging pile count volume | ( public charging pile count /EV has volume ( )) | ≥8.0 | 3.5-6.5 | ≤1.5 | electric operation platform | month | new-energy / city |
| 172 | smart vehicle berth network rate (%) | city smart vehicle platform of berth share | ( network berth count / vehicle berth total count )×100% | ≥65% | 25%-45% | ≤8% | smart vehicle platform | month | city vehicle |

### 3.5 Logistics Hub & Park Infrastructure

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 173 | country logistics hub operation rate (%) | country logistics hub build transport of share | ( operation logistics hub count / plan logistics hub total count )×100% | ≥60% | 30%-48% | ≤12% | mouth department / transport transport manage department count | year | logistics |
| 174 | logistics park / zone smart -isation rate (%) | smart -isation manage system (WMS/TMS etc.) of logistics park / zone share | ( smart -isation park / zone count / logistics park / zone total count )×100% | ≥45% | 18%-32% | ≤5% | in IoT count | year | logistics |
| 175 | logistics automatic -isation min coverage rate (%) | parcel transport enterprise use automatic min equipment of share | ( automatic -isation min process volume / total min volume )×100% | ≥80% | 42%-62% | ≤15% | parcel enterprise count | year | logistics |
| 176 | multimodal efficiency (h) | multimodal container average time | T complete -T arrival | ≤2 | 4-8 | ≥24 | multimodal service platform | day | multimodal |

---

## IV. Mobility Services (65 KPIs)

### 4.1 Public Transport Service

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 177 | transport machine -isation travel min rate (%) | central city transport share of machine -isation travel of share | ( bus travel volume / machine -isation travel total volume )×100% | ≥60% | 40%-52% | ≤25% | travel /IC | year | transport |
| 178 | transport degree (5 min ) | for city public transport service of composite | degree min | ≥4.2 | 3.5-4.0 | ≤2.8 | degree | quarter | transport |
| 179 | transport travel information service coverage rate (%) | real-time to station information service of bus line road / stop / station share | ( real-time information service cover stop / station count / bus stop / station total count )×100% | ≥95% | 65%-82% | ≤30% | travel information platform | year | transport |
| 180 | transport travel APP month rate (%) | transport travel type APP month active users share | ( MAU / service city resident population )×100% | ≥25% | 10%-18% | ≤3% | APP operation data | month | transport |
| 181 | electric coverage rate (%) | bus / support vehicle share | ( support electric count / total count )×100% | ≥98% | 70%-90% | ≤35% | / platform | month | transport |
| 182 | bus accessibility facility coverage rate (%) | accessibility facility of bus vehicle and stop / station share | ( accessibility vehicle / stop / station count / total count )×100% | ≥80% | 42%-65% | ≤15% | bus manage system | year | public bus |
| 183 | rail transit accessibility transfer rate (%) | rail stop / station within accessibility transfer road rate | ( accessibility transfer station count / transfer station total count )×100% | ≥95% | 65%-82% | ≤30% | rail transit manage | year | rail transit |
| 184 | after km coverage rate (%) | rail transit stop / station 800m within has bus / vehicle of share | ( has stop / station count / rail stop / station total count )×100% | ≥90% | 65%-80% | ≤38% | line network GIS | year | rail transit / bus |
| 185 | bus integration rate (%) | government area within bus line road build village share | ( bus build village count / total build village count )×100% | ≥95% | 60%-82% | ≤30% | road transport count | year | bus |
| 186 | bus line road count ( item ) | city at operation of -isation bus line road total count | actual operation of / network bus line road count | ≥200 | 35-120 | ≤5 | bus operation platform | month | demand respond bus |

### 4.2 MaaS & Integrated Mobility Service

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 187 | MaaS platform coverage rate (%) | launched MaaS ( travel i.e. service ) platform of city share | ( has MaaS number of cities / per 10k persons mouth with on number of cities )×100% | ≥40% | 12%-25% | ≤3% | | year | |
| 188 | MaaS platform user rate (%) | MaaS platform month active users share of city person mouth share | ( MAU / city resident population )×100% | ≥15% | 4%-9% | ≤1% | MaaS platform operation data | month | |
| 189 | travel plan accuracy (%) | integrated mobility plan plan time and actual time of deviation | (1-|T actual -T plan |/T actual )×100% | ≥88% | 75%-84% | ≤60% | MaaS / platform | day | |
| 190 | travel coverage rate (%) | support of line road share | ( line road for count / OD for total count )×100% | ≥20% | 5%-12% | ≤1% | / min system | quarter | |
| 191 | sharing vehicle vehicle utilisation rate (%) | sharing vehicle daily average use hr share | ( day total use time /(24× deployed fleet size ))×100% | ≥35% | 20%-28% | ≤8% | sharing vehicle platform | day | shared mobility |
| 192 | ride-hailing -isation rate (%) | ride-hailing share of total share | ( number of trips / total number of trips )×100% | ≥90% | 55%-78% | ≤25% | ride-hailing supervision platform | month | ride-hailing |
| 193 | ride-hailing should time (min) | passenger vehicle after to driver of average waiting time | T -T under | ≤2 | 3-6 | ≥12 | ride-hailing platform | day | ride-hailing |
| 194 | taxi electric rate (%) | taxi network / electric share | ( electric count / total electric count )×100% | ≥85% | 62%-78% | ≤35% | taxi manage platform | day | taxi |
| 195 | bike-share \ compliance rate (%) | bike-share （ electric vehicle ） of share | ( has vehicle count / operation vehicle total count )×100% | ≥95% | 65%-85% | ≤30% | bike-share platform | day | shared mobility |

### 4.3 Expressway Mobility Service

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 196 | expressway information service coverage rate (%) | real-time road information service of expressway distance ratio | ( information service cover distance / total distance )×100% | ≥98% | 75%-90% | ≤45% | mobility service system | year | |
| 197 | service district electric coverage rate (%) | installed electric facility of expressway service district share | ( has electric service district count / service district total count )×100% | ≥90% | 55%-75% | ≤20% | service district manage system | month | |
| 198 | service district Wi-Fi coverage rate (%) | Wi-Fi of service district share | ( has WiFi service district count / service district total count )×100% | ≥85% | 40%-65% | ≤12% | service district manage system | month | |
| 199 | expressway response time (h) | user via line /APP to time of average time | T time -T | ≤1 | 3-8 | ≥24 | passenger service system | day | |
| 200 | ETC service degree (5 min ) | user for ETC complete service of composite | degree min | ≥4.5 | 3.8-4.3 | ≤3.0 | user | quarter | |

### 4.4 Accessible & Inclusive Mobility

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 201 | -isation mobility service coverage rate (%) | transport service APP/ equipment support -isation of share | ( -isation count / total service count )×100% | ≥80% | 35%-55% | ≤10% | service manage platform | quarter | complete |
| 202 | travel information service support rate (%) | transport information service APP/ network station support of share | ( support system count / total count )×100% | ≥70% | 30%-50% | ≤8% | travel information platform | year | complete |

---

## V. Economic Operations (75 KPIs)

### 5.1 Transport Economics — Macro Indicators

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 203 | transport transport value share of GDP proportion (%) | transport, warehousing and postal value share of GDP of share | ( transport transport value /GDP)×100% | ≥5.5% | 4.0%-4.8% | ≤2.5% | count year | year | complete |
| 204 | composite transport ( $100M ) | annual road / water road / railway / civil aviation transport total | Σ each | ≥30000 | 15000-24000 | ≤5000 | transport transport count | year | complete |
| 205 | transport rate ( $10k / person · year ) | transport transport from personnel of year | value / from personnel total count | ≥35 | 20-28 | ≤10 | count year | year | complete |
| 206 | meeting logistics total use share of GDP ratio rate (%) | meeting logistics total use share of GDP of share | ( logistics total use /GDP)×100% | ≤12.0% | 13.5%-15.5% | ≥18.0% | mouth department / in IoT | quarter | logistics |
| 207 | freight transport volume ( 100M tonnes ) | annual complete meeting freight transport total volume | Σ each freight transport volume | ≥550 | 200-400 | ≤50 | transport transport count | month | freight transport |
| 208 | freight transport week volume ( 100M tonnes km) | annual complete meeting freight week total volume | Σ( freight transport volume × average transport ) | ≥220000 | 80000-160000 | ≤15000 | transport transport count | month | freight transport |
| 209 | passenger volume ( 100 million passenger-trips ) | annual complete meeting passenger transport total volume | Σ each passenger volume | ≥180 | 70-130 | ≤15 | transport transport count | month | passenger transport |
| 210 | passenger transport week volume ( person km) | annual complete meeting passenger week total volume | Σ( passenger volume × average transport ) | ≥38000 | 12000-28000 | ≤2500 | transport transport count | month | passenger transport |
| 211 | parcel volume ( ) | annual parcel service enterprise volume | parcel enterprise volume count | ≥1500 | 400-1000 | ≤50 | country postal | month | parcel |
| 212 | transport -isation index (%) | railway / waterway etc. green transport freight transport share | ( railway + waterway freight transport week volume / total week volume )×100% | ≥60% | 38%-48% | ≤22% | transport transport count | year | freight transport |

### 5.2 Operational Efficiency & Cost

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 213 | road freight transport vehicle rate (%) | freight transport vehicle running distance share of total running distance of share | ( distance / total running distance )×100% | ≤18% | 28%-38% | ≥52% | freight transport GP S platform | month | freight transport |
| 214 | road freight transport vehicle rate (%) | freight transport vehicle actual volume share of volume of share | ( actual volume / volume )×100% | ≥75% | 55%-68% | ≤35% | freight transport GP S/ | month | freight transport |
| 215 | bus vehicle daily average operating mileage (km) | bus vehicle standard unit daily average running distance | day total operating mileage / deployed fleet size | ≥180 | 140-165 | ≤90 | bus dispatch system | day | public bus |
| 216 | rail transit veh-km cost ( $ / veh-km) | rail transit veh-km operation cost | year operation total cost /( deployed fleet size × year veh-km) | ≤15 | 18-25 | ≥38 | rail transit | year | rail transit |
| 217 | bus person km cost ( $ / person km) | bus passenger km operation cost | year operation total cost /( year passenger volume × average transport ) | ≤0.35 | 0.50-0.75 | ≥1.20 | bus | year | public bus |
| 218 | expressway ( $10k /km· year ) | expressway km year | year total / distance | ≥1200 | 500-850 | ≤180 | expressway | month | |
| 219 | rail transit coverage rate (%) | for operation cost of cover share | ( / operation total cost )×100% | ≥85% | 55%-72% | ≤25% | rail transit | year | rail transit |
| 220 | port cost ( $ / TEU ) | port standard container average cost | total cost / number of containers handled | ≤80 | 120-180 | ≥350 | port system | month | port |
| 221 | efficiency (L/ per 100 tonne-km ) | per 100 tonne-km volume | volume /( km /100) | ≤25 | 28-33 | ≥42 | driver system | month | civil aviation |
| 222 | freight transport vehicle daily average running distance (km) | transport freight wagon vehicle daily average running distance | (Σ day running distance )/ transport freight wagon count | ≥350 | 200-280 | ≤90 | freight transport GP S platform | day | freight transport |
| 223 | bus line road operation line ratio (%) | bus line road operation can cover can cost of share | ( line road count / total line road count )×100% | ≥45% | 22%-35% | ≤8% | bus system | month | public bus |
| 224 | rail transit share (%) | / commerce /TOD etc. share of operation total of share | ( / operation total )×100% | ≥30% | 12%-22% | ≤3% | rail transit | year | rail transit |

### 5.3 Project Investment & PPP Performance

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 225 | transport PPP project rate (%) | PPP project in complete segment of share | ( PPP project count / warehouse PPP project total count )×100% | ≥55% | 28%-40% | ≤10% | PPP composite information platform | quarter | road / rail transit |
| 226 | transport project investment exceeding compute rate (%) | actual exceeding compute approved metal of project share | ( exceeding compute project count / total project count )×100% | ≤5% | 12%-22% | ≥40% | manage system | year | complete |
| 227 | transport project work hr complete rate (%) | plan work complete ( ) of project share | ( hr complete project count / total project count )×100% | ≥85% | 65%-78% | ≤40% | project manage system | year | complete |
| 228 | expressway build cost ( $100M /km) | expressway km average build cost | total / build distance | ≤0.9 | 1.2-1.8 | ≥3.5 | engineering cost compute data | year | |
| 229 | rail transit build cost ( $100M /km) | city rail transit ( under line ) km average build cost | total / build distance | ≤6.0 | 7.5-10.0 | ≥15.0 | engineering cost compute data | year | rail transit |
| 230 | smart transport project ROI(%) | smart transport economy rate | ( project year -isation effectiveness - year -isation cost )/ total ×100% | ≥18% | 8%-14% | ≤2% | project | year | complete |
| 231 | intelligent transport system O&M cost share (%) | intelligent transport system annual O&M use share of build of share | ( year O&M use / build total )×100% | ≤5% | 8%-15% | ≥25% | O&M system | year | complete |

### 5.4 Road Assets & Maintenance

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 232 | road value maintain rate (%) | and value ratio | ( actual / demand )×100% | ≥92% | 65%-82% | ≤35% | asset management system | year | road |
| 233 | road plan rate (%) | annual plan actual complete share | ( complete engineering count / plan engineering count )×100% | ≥95% | 80%-90% | ≤58% | manage system | month | road |
| 234 | equipment utilisation rate (%) | machine equipment of actual use time and can use time ratio | ( actual operate unit hr / can use unit hr )×100% | ≥72% | 45%-62% | ≤22% | equipment manage system | month | road |
| 235 | road surface property share (%) | property share of total of share | ( property / total )×100% | ≥30% | 12%-22% | ≤3% | manage system | year | road |
| 236 | road assets manage (AM) digital -isation coverage rate (%) | use digital -isation asset management system of road distance share | ( digital asset management system cover distance / total distance )×100% | ≥55% | 18%-35% | ≤3% | asset management system | year | road |
| 237 | road quality rate (%) | engineering quality of share | ( engineering count / engineering total count )×100% | ≥96% | 85%-93% | ≤68% | quality system | quarter | road |

### 5.5 Digital Operations & Service Benefits

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 238 | digital -isation service user rate (%) | use digital -isation transport service (APP/ etc.) of user share | ( digital -isation service user count / resident population )×100% | ≥55% | 22%-38% | ≤8% | digital -isation service platform | month | complete |
| 239 | line on office rate (%) | transport government / operation via line on channel office of share | ( line on office volume / total office volume )×100% | ≥88% | 55%-75% | ≤22% | service platform | month | complete |
| 240 | intelligent passenger service rate (%) | intelligent passenger service user ( none person work ) of share | ( intelligent passenger service volume / total volume )×100% | ≥75% | 45%-62% | ≤18% | passenger service system | day | complete |
| 241 | social media information reach rate (%) | transport information via social media ( WeChat / TikTok etc.) reach of user share | ( social media channel reach user count / target users total count )×100% | ≥30% | 12%-20% | ≤3% | social media operation platform | month | complete |
| 242 | user degree rate (%) | digital -isation service platform month active users year-on-year rate | ( MAU - year MAU )/ year MAU ×100% | ≥25% | 8%-16% | ≤0% | digital -isation service platform | month | complete |

---

## VI. Green & Low-Carbon (55 KPIs)

### 6.1 Carbon Emissions & Energy Use

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 243 | transport transport carbon emissions total volume ( 10k tonnes CO2 ) | transport transport annual -isation carbon emissions total volume | Σ( each energy consumption × carbon emissions due to ) | — | — | — | / transport transport manage department | year | complete |
| 244 | transport transport carbon emissions intensity ( tonnes CO2 / $10k ) | transport transport value carbon emissions volume | carbon emissions total volume / value ( $10k ) | ≤1.8 | 2.8-3.8 | ≥6.0 | / count year | year | complete |
| 245 | transport vehicle transport week volume carbon emissions (kg CO2 / per 100 tonne-km ) | transport freight wagon per 100 tonne-km CO2 | × due to / week volume ( per 100 tonne-km ) | ≤5.5 | 7.0-9.5 | ≥14.0 | energy consumption monitor platform | month | road freight transport |
| 246 | transport passenger vehicle transport carbon emissions (kg CO2 / per 100 passenger-km ) | transport passenger vehicle per 100 passenger-km CO2 | × due to / week volume ( per 100 passenger-km ) | ≤2.0 | 2.8-3.8 | ≥6.0 | energy consumption monitor platform | month | road passenger transport |
| 247 | railway transport carbon emissions (g CO2 / km) | railway freight transport km CO2 | total carbon emissions / freight transport week volume | ≤12 | 15-20 | ≥30 | railway energy consumption count | year | railway |
| 248 | civil aviation transport carbon emissions (g CO2 / person km) | civil aviation passenger transport person km CO2 | total carbon emissions / passenger transport week volume | ≤85 | 95-115 | ≥140 | carbon emissions | month | civil aviation |
| 249 | waterway transport carbon emissions (g CO2 / km) | waterway freight transport km CO2 | total carbon emissions / freight transport week volume | ≤8 | 10-15 | ≥25 | waterway energy consumption count | year | waterway |
| 250 | transport transport energy consumption total volume ( 10k tce ) | transport transport year composite can total volume | Σ each can volume × count | — | — | — | can | year | complete |
| 251 | transport vehicle energy consumption intensity (kg tce / veh-km) | transport vehicle veh-km composite energy consumption | energy consumption total volume /( veh-km /10000) | ≤320 | 420-550 | ≥850 | energy consumption monitor platform | month | road |
| 252 | target with degree (%) | transport transport target cumulative complete degree | ( cumulative volume / volume )×100% | — | — | — | manage platform | year | complete |

### 6.2 Green Travel

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 253 | green travel share (%) | central city use transport + + new-energy vehicle travel share | ( green travel trips / total pedestrian time )×100% | ≥78% | 60%-72% | ≤38% | travel | year | urban traffic |
| 254 | new-energy bus vehicle share (%) | new-energy bus vehicle share of bus vehicle total count of share | ( new-energy bus vehicle count / bus vehicle total count )×100% | ≥85% | 55%-75% | ≤22% | bus manage system | month | public bus |
| 255 | new-energy taxi share (%) | new-energy taxi share of taxi total count share | ( new-energy taxi count / taxi total count )×100% | ≥60% | 18%-40% | ≤5% | taxi manage platform | month | taxi |
| 256 | new-energy logistics vehicle share (%) | city new-energy vehicle share of logistics vehicle of share | ( new-energy vehicle count / vehicle total count )×100% | ≥35% | 8%-20% | ≤2% | logistics manage platform | month | city logistics |
| 257 | port electric coverage rate (%) | electric should capability of port berth share | ( has electric berth count / berth total count )×100% | ≥80% | 35%-58% | ≤10% | port manage system | year | port |
| 258 | machine field APU equipment use rate (%) | flight machine at machine use surface electric / APU of share | ( use equipment time / time )×100% | ≥95% | 65%-85% | ≤30% | machine field operate system | day | civil aviation |
| 259 | city bicycle / bike-share daily average turnover rate ( time / day · vehicle ) | bicycle / bike-share day vehicle use frequency | day use volume / operation volume | ≥3.5 | 1.8-2.8 | ≤0.8 | bicycle / sharing platform | day | active transportation |
| 260 | transport vehicle share (%) | electric / electric etc. bus vehicle share | ( bus vehicle count / bus vehicle total count )×100% | ≥60% | 25%-45% | ≤5% | bus manage system | month | public bus |
| 261 | city green district coverage rate (%) | city or green freight transport district of area share | ( green district area / built-up area )×100% | ≥35% | 8%-18% | ≤2% | green freight transport count | year | city logistics |

### 6.3 Pollution & Environment

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 262 | transport compliance rate (%) | urban road transport reach country value of road segment share | ( compliant road / monitor road total )×100% | ≥85% | 65%-78% | ≤40% | monitor station | quarter | urban road |
| 263 | motor vehicle compliance rate (%) | motor vehicle detect compliant vehicle share | ( detect compliant vehicle count / detect total count )×100% | ≥92% | 78%-88% | ≤58% | motor vehicle detect system | quarter | road |
| 264 | transport control rate (%) | urban road machine -isation area share | ( machine area / road total area )×100% | ≥90% | 65%-80% | ≤35% | health manage system | month | urban road |
| 265 | vessel control district volume compliance rate (%) | vessel use volume meet control district need of share | ( compliant vessel count / detect vessel count )×100% | ≥98% | 85%-95% | ≤62% | enforcement system | month | waterway |
| 266 | road construction environmental protection compliance rate (%) | road construction project environmental protection / compliant of share | ( environmental protection compliant project count / construction project total count )×100% | ≥88% | 68%-82% | ≤38% | construction / monitor | quarter | road |
| 267 | transport water utilisation rate (%) | service district / hub / vehicle etc. transport water using share | ( use water volume / water generate volume )×100% | ≥40% | 15%-28% | ≤3% | environmental protection manage system | year | complete |

### 6.4 Dual-Carbon Management & Markets

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 268 | transport enterprise information rate (%) | on city transport enterprise / country carbon emissions information of share | ( enterprise count / should enterprise count )×100% | ≥65% | 28%-45% | ≤8% | enterprise year /ESG | year | complete |
| 269 | transport transaction and degree (%) | national market or test point market of transport enterprise share | ( and transaction enterprise count / should enterprise count )×100% | ≥45% | 12%-28% | ≤2% | transaction platform | year | complete |
| 270 | expressway machine rate (%) | installed distribution facility of expressway distance share | ( cover road / build road )×100% | ≥8% | 1.5%-4.5% | ≤0.2% | new-energy manage system | year | |
| 271 | for coverage rate (%) | transport vehicle driver / of share | ( cover driver count / transport driver total count )×100% | ≥45% | 15%-30% | ≤3% | for analyse platform | quarter | road |
| 272 | transport low-carbon technology application rate (%) | transport enterprise use and with on low-carbon technology of share | ( use low-carbon technology enterprise count / enterprise total count )×100% | ≥55% | 22%-38% | ≤5% | / count | year | complete |

---

## VII. Data & Intelligence (65 KPIs)

### 7.1 Data Asset Management

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 273 | transport data resources cover degree (%) | data resources of data share of complete data share | ( data count / identify data total count )×100% | ≥85% | 42%-62% | ≤12% | data platform | month | complete |
| 274 | data standard rate (%) | transport data country / / enterprise data standard of share | ( standard data item count / data item total count )×100% | ≥92% | 65%-82% | ≤35% | data governance platform | quarter | complete |
| 275 | data quality composite min ( min ) | data property + property + property + timely property + property composite min | min ( / / / timely / ) | ≥92 | 72-85 | ≤48 | data governance platform | month | complete |
| 276 | data warehouse latency (min) | from data generate to can use of average latency | T can -T generate | ≤0.5 | 2-10 | ≥30 | data platform | real-time | complete |
| 277 | data rate (%) | data in / value / anomaly value share | ( anomaly data item count / total data item count )×100% | ≤1% | 3%-8% | ≥18% | data governance platform | day | complete |
| 278 | data property (%) | system data ( vehicle / personnel / equipment etc.) of degree | ( data item count / data total count )×100% | ≥98% | 82%-93% | ≤60% | MDM data platform | month | complete |
| 279 | data coverage rate (%) | data item capability of share | ( has data of data item / data item total count )×100% | ≥80% | 32%-55% | ≤8% | data governance platform | quarter | complete |
| 280 | data cycle manage rate (%) | data cycle ( collect / at rest / / ) manage of data share | ( manage data count / data total count )×100% | ≥88% | 45%-68% | ≤15% | data manage platform | quarter | complete |

### 7.2 Data Sharing & Open Data

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 281 | open data rate (%) | with API/ culture etc. to meeting open of data share of can open data share | ( open data count / can open data count )×100% | ≥45% | 15%-28% | ≤3% | open data platform | quarter | complete |
| 282 | data sharing mouth use volume ( time / day ) | transport data sharing platform daily average API mouth use volume | day API use total volume ( time ) | ≥500 | 50-200 | ≤5 | data sharing platform | day | complete |
| 283 | department data sharing meet rate (%) | department data demand actual to meet of share | ( meet data demand count / data demand total count )×100% | ≥78% | 45%-65% | ≤18% | data sharing platform | month | complete |
| 284 | data sharing timeliness (min) | data from receive demand to complete sharing of average time | T sharing complete -T demand receive | ≤15 | 45-90 | ≥360 | data sharing platform | month | complete |
| 285 | data assets -isation rate (%) | complete data assets assess / of data assets share of can -isation data of share | ( -isation data item / can -isation data item )×100% | ≥25% | 5%-15% | ≤0.5% | data assets manage | year | complete |
| 286 | data trading volume ( $10k ) | transport data at data trading / platform of year transaction metal | year data trading total metal | ≥5000 | 500-1500 | ≤50 | data trading platform | month | complete |
| 287 | calculate technology use rate (%) | use study / safety calculate etc. calculate technology of data sharing field share | ( use calculate field count / agency sharing field total count )×100% | ≥20% | 3%-10% | ≤0.3% | data platform | year | complete |

### 7.3 AI Models & Algorithms

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 288 | AI model count volume ( unit ) | transport field in launched operate of AI model total count | at use AI model count volume | ≥150 | 25-80 | ≤5 | AI model manage platform | month | complete |
| 289 | model accuracy (%) | AI model at actual in of composite accuracy | ( time count / total time count )×100% | ≥95% | 82%-92% | ≤65% | AI model platform | day | complete |
| 290 | model latency (ms) | AI model time average response time | - response time | ≤50 | 100-300 | ≥1000 | AI model platform | day | complete |
| 291 | model detect rate (%) | detect model property can of cover share | ( detect model count / online model total count )×100% | ≥90% | 55%-75% | ≤20% | model manage platform | month | complete |
| 292 | model frequency ( time / month ) | AI model month new time count | month model new total time count / model count | ≥4 | 1-2 | ≤0.25 | model manage platform | month | complete |
| 293 | AI model use rate (%) | model group / can field use of share | ( can use model group count / model group total count )×100% | ≥55% | 25%-40% | ≤8% | model manage platform | quarter | complete |
| 294 | model transport field application cover count ( unit ) | transport model ( such as LLM/ ) cover of min field count | of transport model application field count | ≥30 | 5-15 | ≤1 | AI manage platform | quarter | complete |
| 295 | AI rate (%) | based on AI analyse build by ( person work ) of share | ( by build count /AI build total count )×100% | ≥65% | 30%-48% | ≤8% | support system | month | complete |
| 296 | intelligent analyse accuracy (%) | transport AI analyse ( vehicle / pedestrian / event identify ) of composite accuracy | ( analyse count / total analyse count )×100% | ≥95% | 82%-92% | ≤62% | AI platform | day | road |
| 297 | NLP transport intelligent accuracy (%) | transport process of accuracy | ( count / total count )×100% | ≥88% | 65%-78% | ≤38% | intelligent platform | day | complete |

### 7.4 Cloud Computing & Platform Capability

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 298 | transport cloud platform resources utilisation rate (%) | CPU/ within / at rest / GP U etc. resources average utilization | ( actual use resources / min resources )×100% | ≥65% | 35%-52% | ≤15% | cloud manage platform | day | complete |
| 299 | platform service can use rate (%) | transport digital platform ( composite traffic operation in / data platform etc.) of can use property | ( can use time / total time )×100% | ≥99.99% | 99.90%-99.95% | ≤99.50% | O&M platform | day | complete |
| 300 | platform mouth response time (ms) | data / service API of average response time (95 percentile ) | HTTP API P95 response time | ≤200 | 500-1000 | ≥3000 | API network /APM | day | complete |
| 301 | data platform day process data volume (TB) | transport data platform daily average data process volume | day process data volume TB | ≥100 | 15-55 | ≤2 | data platform | day | complete |
| 302 | data process latency (ms) | data from generate to process process of end-to-end latency | T process -T generate | ≤100 | 500-2000 | ≥10000 | calculate platform | real-time | complete |
| 303 | cloud application share (%) | use /K8S/ service of transport system share | ( cloud application count / application total count )×100% | ≥65% | 22%-45% | ≤5% | cloud manage /DevOps platform | quarter | complete |
| 304 | system switch time (min) | data in failure hr switch to in of RTO | T manage -T in failure | ≤5 | 15-30 | ≥120 | manage platform | | complete |
| 305 | RPO data volume (min) | occur hr can can of maximum data hr | switch after data time deviation | ≤1 | 5-15 | ≥60 | manage platform | | complete |

### 7.5 Digital Twin & CIM

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 306 | digital twin road network coverage rate (%) | build digital twin model of road / hub / terminal / depot distance or area share | ( digital twin cover road / road network total )×100% | ≥45% | 8%-22% | ≤1% | digital twin platform | year | road |
| 307 | digital twin model degree ( ) | digital twin model reach of LOD etc. (Level of Detail) | LOD1-LOD5 | LOD4+ | LOD3 | LOD1-2 | digital twin platform | year | road |
| 308 | digital twin data new frequency ( time /min) | digital twin field transport data new frequency | data new time count / min | ≥12 | 3-6 | ≤0.5 | digital twin platform | real-time | road |
| 309 | transport simulation model degree (%) | transport simulation ( travel time / delay ) and actual deviation | 1-| simulation value - measure value |/ measure value ×100% | ≥90% | 75%-85% | ≤55% | transport simulation system | month | urban road |
| 310 | CIM convergence data type count ( type ) | city information model in convergence of transport data type | data type plan count | ≥80 | 25-55 | ≤8 | CIM / digital twin platform | year | urban traffic |

---

## VIII. Organisation & Governance (55 KPIs)

### 8.1 Institutions & Operating Framework

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 311 | composite transport complete degree ( min ) | city / area composite transport manage degree assess min | assess / min | ≥90 | 65-80 | ≤40 | institution / system assess | year | urban traffic |
| 312 | transport law sports rate (%) | unit property transport law / cover should cover of share | ( has law count / should cover count )×100% | ≥85% | 55%-72% | ≤25% | law data warehouse | year | complete |
| 313 | composite transport planning rate (%) | composite transport planning in point project / indicator of annual rate | ( project count / plan project count )×100% | ≥90% | 65%-82% | ≤35% | plan manage system | year | complete |
| 314 | transport data manage organise complete degree | is has data manage department /CDO and data personnel | assess min ( organise + + personnel ) | ≥85 | 50-72 | ≤25 | organise assess | year | complete |
| 315 | department meeting frequency ( time / quarter ) | transport / manage / plan / work information etc. department composite transport meeting frequency | quarterly meeting time count | ≥2 | 1 | 0 | government record | quarter | complete |
| 316 | transport data operation degree | operation of institution / system / platform / supervision etc. degree | based on assess model min | ≥80 | 40-62 | ≤15 | institution / system / platform assess | year | complete |

### 8.2 Talent & Capability Building

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 317 | transport digital -isation talent share (%) | from data /AI/ information -isation work as of work share of transport agency total person count share | ( digital -isation personnel count / agency total person count )×100% | ≥12% | 3%-8% | ≤0.8% | HR system | year | complete |
| 318 | transport from personnel year study hr (h) | transport from personnel year / education study hr | Σ study hr / from personnel total count | ≥60 | 24-42 | ≤8 | manage system | year | complete |
| 319 | digital -isation can coverage rate (%) | digital -isation / data /AI can of work share | ( digital -isation person count / total work count )×100% | ≥65% | 18%-40% | ≤3% | manage system | year | complete |
| 320 | AI/ data talent rate (%) | annual new AI/ data talent share of all new personnel of share | ( new AI/ data talent count / new total person count )×100% | ≥20% | 5%-12% | ≤1% | HR system | year | complete |
| 321 | transport innovation platform count ( unit ) | transport enterprise / agency build of province with on platform count | country point / engineering in / enterprise technology in count volume | ≥10 | 2-6 | ≤1 | manage count | year | complete |
| 322 | density ( / per 1k persons · year ) | work year / count volume | ( year + count )/( work count /1000) | ≥25 | 5-15 | ≤1 | system | year | complete |

### 8.3 Standards & Specifications

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 323 | enterprise standard count ( item / year ) | transport enterprise / agency year or and of each type standard count volume | annual / and standard total count | ≥15 | 3-10 | ≤1 | standard -isation manage system | year | complete |
| 324 | standard coverage rate (%) | as standard / enterprise standard of share | ( count / should total count )×100% | ≥92% | 65%-82% | ≤32% | manage system | year | complete |
| 325 | country standard and degree ( item ) | cumulative / and ISO/ITU/IEEE etc. country standard count volume | at + publish country standard count | ≥5 | 0-2 | 0 | country standard organise | year | complete |
| 326 | country -isation standard rate (%) | information -isation system / country -isation need standard of share | ( country -isation system count / assess system total count )×100% | ≥85% | 35%-60% | ≤8% | country -isation manage system | quarter | complete |

### 8.4 Funding & Investment

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 327 | transport digital -isation share of total ratio (%) | digital -isation / information -isation build share of transport total of proportion | ( digital -isation / information -isation / transport total )×100% | ≥5% | 1.8%-3.5% | ≤0.5% | manage system | year | complete |
| 328 | intensity (%) | transport enterprise / agency share of / compute of share | ( / total )×100% | ≥8% | 2.5%-5.0% | ≤0.8% | system | year | complete |
| 329 | transport item compute to rate (%) | annual compute in transport / digital -isation item compute of to share | ( actual to funding / compute approved metal )×100% | ≥95% | 75%-88% | ≤48% | system | year | complete |
| 330 | digital -isation project effectiveness project coverage rate (%) | complete effectiveness project of digital -isation project share of complete project of share | ( project project count / complete project count )×100% | ≥65% | 22%-42% | ≤5% | project manage system | year | complete |

### 8.5 Safety & Emergency Management

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 331 | emergency respond coverage rate (%) | item emergency of transport risk field share of identify risk field share | ( has field count / identify risk field total count )×100% | ≥90% | 55%-72% | ≤20% | emergency manage system | year | complete |
| 332 | emergency rate (%) | time complete emergency of share | ( count / total count )×100% | ≥95% | 68%-85% | ≤32% | emergency manage system | year | complete |
| 333 | emergency resources ( equipment / personnel ) to time (min) | from emergency refers to under reach resources arrival field of average time | T resources arrival -T refers to under | ≤15 | 25-40 | ≥90 | emergency refers to system | event | complete |
| 334 | traffic operation monitor coverage rate (%) | by traffic operation monitor system of transport infrastructure / service share | ( monitor facility / service count / facility / service total count )×100% | ≥90% | 55%-75% | ≤22% | operate monitor platform | month | complete |
| 335 | day transport ensure capability index | at item under transport operate of ensure capability min | assess min ( / resources / / ) | ≥85 | 55-72 | ≤30 | emergency capability assess | year | complete |

### 8.6 Performance Assessment & Evaluation

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 336 | performance assessment digital -isation coverage rate (%) | via digital -isation platform perform assess of share | ( digital -isation count / total count )×100% | ≥78% | 32%-52% | ≤8% | manage system | quarter | complete |
| 337 | service etc. SLA rate (%) | IT/ digital service SLA indicator actual share | (SLA compliant service item count /SLA total item count )×100% | ≥98% | 88%-95% | ≤72% | ITSM system | month | complete |
| 338 | user degree index ( min ) | transport digital -isation service user / city degree composite min | / online degree ( min ) | ≥88 | 68-80 | ≤48 | degree platform | quarter | complete |
| 339 | transport transport manage department composite ratio | at province / national property transport transport manage department composite in of | annual / | A / before 20% | B / in | D / after 20% | performance assessment system | year | complete |
| 340 | count ( item / year ) | annual province and with on ( meeting ) count volume | annual total count | ≥8 | 1-4 | 0 | manage count | year | complete |

---

## IX. Logistics & Freight (55 KPIs)

### 9.1 Freight Efficiency & Effectiveness

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 341 | road freight transport vehicle daily average running distance (km) | transport freight wagon daily average running distance | Σ day running distance / transport freight wagon count | ≥350 | 200-280 | ≤90 | freight transport GP S platform | day | road freight transport |
| 342 | freight transport vehicle distance utilisation rate (%) | freight distance share of total running distance ratio | ( freight distance / total distance )×100% | ≥82% | 62%-75% | ≤38% | freight transport GP S platform | month | road freight transport |
| 343 | freight transport vehicle etc. freight time (h) | freight wagon at freight from arrival freight of average waiting time | T freight -T arrival | ≤2 | 4-8 | ≥24 | freight transport dispatch platform | day | road freight transport |
| 344 | freight transport hr rate (%) | freight at time range within arrival freight point of share | ( hr count / total transport count )×100% | ≥96% | 82%-92% | ≤62% | transport manage system (TMS) | day | road freight transport |
| 345 | water transport volume share (%) | water transport container volume share of total container transport volume of share | ( water transport volume / total container transport volume )×100% | ≥8% | 2.5%-5.0% | ≤0.8% | multimodal platform | month | railway / waterway |
| 346 | multimodal share (%) | multimodal complete freight transport volume share of total freight transport volume of share ( week volume ) | ( multimodal week volume / total week volume )×100% | ≥15% | 3%-8% | ≤1% | transport transport count | year | multimodal |
| 347 | freight transport platform user rate (%) | network freight transport / freight transport platform day vehicle share of vehicle ratio | (DAU vehicle count / vehicle count )×100% | ≥55% | 28%-42% | ≤8% | freight transport platform operation | day | road freight transport |
| 348 | transport ratio | vehicle and vehicle count volume ratio | vehicle count / vehicle count | ≥1:2.5 | 1:1.2-1.8 | ≤1:0.8 | vehicle manage system | month | road freight transport |
| 349 | expressway freight wagon ETC use rate (%) | expressway freight wagon use ETC of share | ( freight wagon ETC time count / freight wagon total time count )×100% | ≥75% | 40%-60% | ≤15% | ETC system | month | expressway |
| 350 | city rate (%) | city complete of volume share of total volume share | ( volume / total volume )×100% | ≥38% | 12%-25% | ≤3% | city green freight transport count | year | city logistics |

### 9.2 Logistics Information Service & Visibility

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 351 | logistics information platform coverage rate (%) | logistics information platform ( or network freight transport platform ) of enterprise share | ( platform enterprise count / logistics enterprise total count )×100% | ≥55% | 18%-38% | ≤3% | logistics information platform | year | logistics |
| 352 | freight complete visualisation rate (%) | logistics in freight / status complete can of transport share | ( visualisation transport count / total transport count )×100% | ≥88% | 42%-65% | ≤12% | logistics platform (IoT) | day | logistics |
| 353 | electric transport coverage rate (%) | use electric transport manage of transport share | ( electric transport count / total transport count )×100% | ≥85% | 38%-62% | ≤10% | transport manage system | month | logistics |
| 354 | logistics anomaly event warning accuracy (%) | transport / / etc. anomaly event prediction accuracy | ( warning anomaly count / actual anomaly count )×100% | ≥82% | 55%-72% | ≤28% | logistics anomaly | day | logistics |
| 355 | anomaly event automatic process rate (%) | logistics anomaly event by system automatic process ( none person work ) of share | ( automatic process anomaly count / anomaly event total count )×100% | ≥45% | 12%-28% | ≤2% | logistics anomaly | day | logistics |

### 9.3 Warehousing & Nodes

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 356 | warehousing week day count ( day ) | warehouse from to of average day count | Σ( day - day )/ warehouse time count | ≤7 | 12-22 | ≥45 | warehousing manage system (WMS) | day | logistics warehousing |
| 357 | warehousing warehouse accuracy (%) | warehouse system surface data and actual warehouse rate | ( SKU count / total SKU count )×100% | ≥99.5% | 97%-99% | ≤93% | WMS point | month | logistics warehousing |
| 358 | warehousing utilisation rate (%) | warehouse actual use area / sports and can use area / sports ratio | ( actual use area / can use area )×100% | ≥88% | 65%-80% | ≤38% | WMS | month | logistics warehousing |
| 359 | accuracy (%) | freight of accuracy | ( number of trips / total number of trips )×100% | ≥99.9% | 99.0%-99.6% | ≤97.0% | WMS | day | logistics warehousing |
| 360 | automatic -isation warehouse share (%) | use automatic -isation sports warehouse /AGV etc. automatic -isation equipment of warehouse area share | ( automatic -isation warehouse area / total warehouse area )×100% | ≥35% | 8%-20% | ≤1.5% | warehousing manage count | year | logistics warehousing |
| 361 | warehousing person ( / person · h ) | warehouse as personnel work hr / count | total as count /( person count × work hr ) | ≥180 | 80-130 | ≤30 | WMS | day | logistics warehousing |

### 9.4 Cold Chain & Specialized Logistics

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 362 | cold chain transport compliance rate (%) | cold chain transport complete degree at range within of time share | ( compliant transport hr / total transport hr )×100% | ≥98% | 82%-93% | ≤60% | cold chain IoT system | day | cold chain logistics |
| 363 | cold chain rate (%) | cold chain logistics in degree exceeding or in of share | ( occur number of trips / total number of trips )×100% | ≤0.5% | 2%-6% | ≥15% | cold chain system | day | cold chain logistics |
| 364 | -isation transport electric transport use rate (%) | -isation transport in use electric transport of share | ( electric transport transport time / total transport time )×100% | ≥95% | 62%-85% | ≤28% | -isation supervision platform | month | -isation logistics |
| 365 | -isation transport vehicle online rate (%) | -isation transport vehicle real-time online / of share | ( online vehicle count / -isation vehicle total count )×100% | ≥98% | 78%-92% | ≤45% | -isation supervision platform | day | -isation logistics |
| 366 | parcel after km rate (%) | parcel time ( not economy time ) of share | ( time count / total count )×100% | ≥95% | 82%-90% | ≤65% | parcel enterprise count | day | parcel |

### 9.5 Postal & Parcel

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 367 | parcel complete timeliness (h) | parcel from to of average timeliness | Σ( time - time )/ count | ≤24 | 36-52 | ≥75 | parcel enterprise operation system | day | parcel |
| 368 | parcel rate ( / ) | parcel service in effective count | ( effective count / volume ( )) | ≤1.0 | 3.0-8.0 | ≥25.0 | country postal 12305 | month | parcel |
| 369 | parcel electric surface use rate (%) | parcel use electric transport ( surface ) of share | ( electric surface count / total count )×100% | ≥98% | 85%-95% | ≤55% | parcel enterprise count | month | parcel |
| 370 | parcel intelligent parcel coverage rate ( mouth / per 1k persons ) | resident population has of intelligent mouth count | intelligent parcel mouth count /( resident population /1000) | ≥30 | 10-22 | ≤3 | country postal / enterprise | year | parcel |
| 371 | parcel green -isation rate (%) | use green / can / can of share | ( green count / total count )×100% | ≥65% | 25%-45% | ≤8% | parcel enterprise count | month | parcel |
| 372 | country parcel share (%) | country / unit parcel volume share of total volume share | ( country parcel volume / total volume )×100% | ≥3.5% | 1.5%-2.5% | ≤0.5% | country postal | month | parcel |
| 373 | min automatic -isation rate (%) | automatic min equipment process volume share of total process volume share | ( automatic min count / total min count )×100% | ≥85% | 50%-72% | ≤18% | parcel enterprise count | year | parcel |
| 374 | parcel village coverage rate (%) | parcel service of build village share of complete build village share | ( parcel build village count / build village total count )×100% | ≥98% | 78%-92% | ≤48% | country postal | month | parcel |

### 9.6 Cross-border Logistics & Supply Chain

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 375 | in shift operated trips ( / year ) | annual in shift total volume | complete year operated trips | ≥18000 | 8000-13000 | ≤1000 | country / country infrastructure as | month | railway |
| 376 | in shift rate (%) | in shift container ( ) trips share | ( trips / total operated trips )×100% | ≥98% | 88%-95% | ≤72% | country | month | railway |
| 377 | cross-border transport customs clearance timeliness (h) | road / railway mouth mouth freight average customs clearance time | T -T transport | ≤2 | 6-15 | ≥48 | Single Window | month | cross-border logistics |
| 378 | country Single Window coverage rate (%) | country " Single Window " need application rate | ( Single Window process volume / total volume )×100% | ≥95% | 52%-78% | ≤20% | country Single Window | month | complete |
| 379 | supply chain visualisation rate (%) | supply chain on under node with information interchange can of share | ( visualisation supply chain count / total count )×100% | ≥65% | 22%-42% | ≤5% | supply chain manage platform | quarter | logistics |

---

## X. Cross-Modal Integration (42 KPIs)

### 10.1 Multimodal Transport

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 380 | multimodal " " coverage rate (%) | use multimodal documents ( to ) of share | ( transport count / multimodal total transport count )×100% | ≥35% | 5%-18% | ≤0.5% | multimodal platform | month | multimodal |
| 381 | multimodal information interchange rate (%) | not transport complete data of node share | ( node for count / should node for total count )×100% | ≥65% | 18%-40% | ≤3% | multimodal information platform | year | multimodal |
| 382 | multimodal EDI/API standard -isation rate (%) | use standard electric data / mouth of transport share | ( use standard EDI/API of / total )×100% | ≥75% | 25%-48% | ≤5% | multimodal platform | year | multimodal |
| 383 | transport in time (h) | not transport freight in average waiting time | T under -T on arrival | ≤4 | 8-16 | ≥48 | multimodal service platform | day | multimodal |
| 384 | multimodal enterprise as index | multimodal economy person / transport person coordination of degree | composite ( information system for / standard / operation ) | ≥80 | 42-65 | ≤18 | | year | multimodal |

### 10.2 Integrated Transport Hub Integration

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 385 | hub composite information service degree (%) | hub within not transport information service sharing of share | ( information type count / information type total count )×100% | ≥85% | 38%-62% | ≤10% | hub information platform | year | composite hub |
| 386 | hub dispatch coordination rate (%) | hub within not transport operation dispatch coordination of automatic -isation degree | automatic -isation min (0-100) | ≥70 | 25-48 | ≤5 | hub dispatch system | month | composite hub |
| 387 | hub emergency linkage timeliness (min) | hub sudden event under transport coordination emergency response time | T coordination respond -T incident occurs | ≤8 | 15-28 | ≥55 | hub emergency system | event | composite hub |
| 388 | hub passenger prediction accuracy (%) | hub to passenger flow hr predict (15min-1h) accuracy | MAPE | ≥92% | 78%-88% | ≤58% | hub passenger predict system | day | composite hub |
| 389 | hub service -isation rate (%) | hub within not transport user surface / service of cover share | ( integration service field count / total service field count )×100% | ≥55% | 12%-28% | ≤2% | hub service platform | year | composite hub |

### 10.3 Urban-Rural Transport Integration

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 390 | bus integration rate (%) | city bus line road / cover week town / build village of share | ( bus cover build village count / build village total count )×100% | ≥92% | 48%-72% | ≤15% | road transport count | year | bus |
| 391 | logistics rate (%) | city and agriculture village logistics network sharing share | ( network point count / total network point count )×100% | ≥55% | 12%-30% | ≤2% | logistics manage | year | logistics |
| 392 | county 30 min on rate (%) | county built-up area 30 min within can expressway of share | (30min within can of county count / county total count )×100% | ≥85% | 55%-72% | ≤28% | road network GIS analyse | year | road |
| 393 | town with on road rate (%) | and with on etc. road of town share | ( and with on road town count / town total count )×100% | ≥90% | 55%-75% | ≤22% | road count | year | road |

### 10.4 Cross-regional Transport Coordination

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 394 | cross-regional transport information sharing rate (%) | city / province transport data / information sharing cover of field share | ( sharing field count / can sharing field total count )×100% | ≥45% | 12%-28% | ≤2% | area transport coordination platform | year | cross-regional |
| 395 | cross-regional signal coordination control rate (%) | city area signal coordination control cover share | ( coordination control intersection count / intersection total count )×100% | ≥35% | 5%-18% | ≤0.5% | signal control system | year | cross-regional |
| 396 | province station ETC province transaction success rate (%) | province ETC province transaction success rate | ( province transaction count / province total transaction count )×100% | ≥99.8% | 98.5%-99.5% | ≤96.0% | ETC national network system | day | |
| 397 | area traffic situation coverage rate (%) | with area traffic situation analyse of city / city share | ( has city count / country point city total count )×100% | ≥40% | 10%-22% | ≤2% | area transport coordination platform | year | cross-regional |
| 398 | province transport enforcement complete rate (%) | province traffic violation / crash complete of ratio rate | ( complete count / total count )×100% | ≥85% | 55%-72% | ≤28% | transport enforcement system | month | cross-regional |

### 10.5 Emergency Transport Assurance

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 399 | transport information resources sharing rate (%) | transport data and transport demand sharing of cover share | ( sharing data / transport demand data )×100% | ≥55% | 18%-35% | ≤3% | transport information system | year | complete |
| 400 | emergency transport compliance rate (%) | need of emergency passenger freight transport share of should volume share | ( actual transport / should transport )×100% | ≥95% | 72%-88% | ≤42% | emergency manage system | year | complete |
| 401 | / emergency road rate (%) | point / emergency road technology status of share | ( road degree / point road total )×100% | ≥92% | 75%-88% | ≤50% | road manage system | quarter | road |

### 10.6 New Technology Convergence

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 402 | V2X district count volume ( unit ) | build or at build of V2X ( autonomous driving ) district count volume | national property + province + city district total count | ≥60 | 15-35 | ≤3 | manage department / transport transport manage department count | year | V2X |
| 403 | autonomous driving measure test distance ( km) | L4 autonomous driving cumulative road measure test distance | cumulative measure test total distance ( km) | ≥8000 | 500-2500 | ≤20 | autonomous driving measure test count | quarter | autonomous driving |
| 404 | intelligent network vehicle rate (%) | V2X communications capability of volume new vehicle share | (V2X new vehicle count / new vehicle total volume )×100% | ≥15% | 2%-8% | ≤0.2% | manage department count | year | V2X |
| 405 | digital twin transport covered area (km²) | city digital twin transport platform cover built-up area | digital twin covered area | ≥500 | 50-200 | ≤5 | digital twin platform | year | urban traffic |
| 406 | transport $ field application count ( unit ) | at / plan / sports etc. field AR/VR/MR application of count volume | actual field plan count | ≥15 | 2-8 | 0 | innovation application manage | year | complete |
| 407 | district logistics documents coverage rate (%) | use district technology manage of multimodal / documents share | ( district documents count / documents total count )×100% | ≥8% | 1%-3% | ≤0.05% | district platform | quarter | logistics / multimodal |
| 408 | transport AI model field cover count ( unit ) | transport use model cover of min application field count | transport model actual application field plan count | ≥35 | 5-18 | ≤1 | AI manage platform | quarter | complete |
| 409 | city intelligent transport manage system rate (%) | flight transport manage capability of city share | ( has ATC system number of cities / city total count )×100% | ≥12% | 1%-5% | ≤0.1% | civil aviation / manage department count | year | transport |
| 410 | transport transport carbon-incentive platform cover number of cities ( unit ) | launched transport carbon-incentive ( MaaS credits etc.) of number of cities volume | launched city plan count | ≥35 | 5-18 | ≤1 | transport carbon-incentive count | year | urban traffic |
| 411 | transport data elements marketisation transaction ( $10k/year ) | transport data as for elements exchange of year transaction scale | year data trading | ≥10000 | 500-3000 | ≤20 | data trading platform | year | complete |

---

## XI. International Benchmark Extension (159 KPIs)

> Additional globally-benchmarked KPIs drawn from ISO 37120, ITF, FHWA HPMS, the EU Urban Mobility Framework, Vision Zero, the World Bank LPI, ACI and port/rail KPI sets. Benchmarks reflect leading (best-practice), median and lagging international peer ranges.

| # | KPI Name | Definition | Formula | Leading Benchmark | Median Benchmark | Lagging Benchmark | Data Source | Collection Frequency | Applicable Modality |
|------|---------|------|----------|------------|------------|------------|----------|----------|----------|
| 412 | Intersection Volume-to-Capacity ratio | V/C of critical movement at signalised intersections | V/C = demand flow / saturation flow | ≤0.85 | 0.90-0.95 | ≥1.00 | Traffic signal system | Per cycle | Urban road |
| 413 | Arterial corridor travel speed (km/h) | Average running speed along a primary arterial | Σ(link length × link speed)/Σ link length | ≥35 | 24-32 | ≤18 | Probe-vehicle GPS | 5 min | Urban road |
| 414 | Transit mode share (%) | Share of motorised trips by public transport | PT trips / total motorised trips ×100% | ≥50% | 25-40% | ≤12% | Household travel survey | Annual | Public transport |
| 415 | Bus commercial speed (km/h) | Bus revenue speed including stops | Route distance / total trip time | ≥20 | 15-18 | ≤10 | AVL / GTFS-realtime | Daily | Public bus |
| 416 | Heavy-rail punctuality (%) | Trains arriving within 5 min of timetable | On-time trains / total trains ×100% | ≥98% | 95-97% | ≤90% | Rail dispatch system | Daily | Rail transit |
| 417 | Airport on-time performance (%) | Flights departing/arriving within 15 min of schedule | On-time flights / total flights ×100% | ≥85% | 75-82% | ≤65% | Airport operations system | Daily | Civil aviation |
| 418 | Port vessel turnaround time (h) | Time from berth arrival to departure | Departure time − berth arrival | ≤18 | 24-36 | ≥60 | Port management system | Daily | Port & waterway |
| 419 | Container terminal berth productivity (moves/h) | Crane moves per ship hour | Total crane moves / ship hours | ≥35 | 25-32 | ≤18 | Terminal operating system | Shift | Port & waterway |
| 420 | Rail freight transit time reliability (%) | Arrival within planned window | On-time freight trains / total ×100% | ≥95% | 88-93% | ≤80% | Railway dispatch system | Daily | Railway |
| 421 | Average commute time (min) | Mean one-way commute duration | Σ commute time / commuters | ≤25 | 30-40 | ≥55 | Household travel survey | Annual | Urban traffic |
| 422 | Road network total VMT (millions) | Annual vehicle-miles travelled on the network | Σ link VMT | — | — | — | HPMS / traffic detectors | Annual | Road |
| 423 | Vehicle occupancy rate (pers/veh) | Average persons per vehicle in peak | Total persons / total vehicles | ≥1.4 | 1.1-1.3 | ≤1.0 | Screen-line survey | Peak | Urban road |
| 424 | Parking occupancy rate (%) | Occupied spaces vs supply in CBD | Occupied / total spaces ×100% | ≤75% | 80-90% | ≥97% | Smart parking platform | Hourly | Urban parking |
| 425 | Bike-share daily trips per capita | Daily bike-share trips per resident | Daily trips / population | ≥0.15 | 0.05-0.10 | ≤0.02 | Bike-share platform | Daily | Active transportation |
| 426 | EV charging availability (%) | Vehicles able to charge within 5 min drive | Served demand / total demand ×100% | ≥95% | 80-90% | ≤60% | Charging operations platform | Daily | New-energy / Urban |
| 427 | Ramp metering benefit (%) | Mainline speed gain from ramp control | (after − before)/before ×100% | ≥20% | 8-15% | ≤0% | Ramp control system | Daily | Expressway |
| 428 | Travel Time Index (TTI) — network | Network actual vs free-flow travel time | Network TTI = actual / free-flow | ≤1.20 | 1.30-1.45 | ≥1.70 | GPS probe data | 15 min | Urban road |
| 429 | Bus bunching rate (%) | Share of trips with >2 buses arriving together | Bunched events / total ×100% | ≤5% | 10-20% | ≥35% | AVL system | Daily | Public bus |
| 430 | Truck travel time reliability (%) | Freight trips within planned window | On-time truck trips / total ×100% | ≥90% | 80-88% | ≤70% | Freight GPS platform | Daily | Road freight |
| 431 | Intermodal transfer time (min) | Average transfer between rail and road freight | Σ transfer time / transfers | ≤30 | 45-90 | ≥180 | Multimodal platform | Daily | Multimodal |
| 432 | Road fatalities per 100k population | Annual road deaths per 100k residents | Deaths / population ×100k | ≤2.5 | 6-9 | ≥15 | Police / ITS data | Annual | Road |
| 433 | Road fatalities per billion VKT | Deaths per billion vehicle-km | Deaths / VKT(bn) | ≤3.0 | 5-8 | ≥12 | Police / HPMS | Annual | Road |
| 434 | Killed-or-Seriously-Injured (KSI) rate | KSI per 100k population | KSI / population ×100k | ≤10 | 30-60 | ≥120 | Police crash stats | Annual | Road |
| 435 | Child road casualties per 100k children | Child KSI per 100k children | Child KSI / child pop ×100k | ≤3 | 10-20 | ≥40 | Police crash stats | Annual | Urban road |
| 436 | Pedestrian fatality rate per 100k | Pedestrian deaths per 100k pop | Ped KSI / pop ×100k | ≤1.0 | 3-5 | ≥10 | Police crash stats | Annual | Active transportation |
| 437 | Cyclist fatality rate per 100k | Cyclist deaths per 100k pop | Cyclist KSI / pop ×100k | ≤0.8 | 2-4 | ≥8 | Police crash stats | Annual | Active transportation |
| 438 | Serious-injury rate reduction (%) | Year-on-year reduction in serious injuries | (prev − curr)/prev ×100% | ≥6% | 2-4% | ≤0% | Police crash stats | Annual | Road |
| 439 | Speed limit compliance (%) | Vehicles within posted limit | Compliant / observed ×100% | ≥90% | 75-85% | ≤60% | Speed camera system | Hourly | Road |
| 440 | Seat-belt wearing rate (%) | Occupants wearing belts | Belted / total ×100% | ≥98% | 90-95% | ≤80% | Roadside survey | Daily | Road |
| 441 | Helmet use rate (%) | Powered-two-wheeler helmet use | Helmeted / total ×100% | ≥95% | 70-85% | ≤50% | Roadside survey | Daily | Road |
| 442 | Vision Zero plan adoption | Whether a endorsed vision-zero plan exists | Binary (yes/no) | Yes | Partial | No | Governance records | Annual | All modalities |
| 443 | Average crash response time (min) | Time to clear a crash after detection | Clear time − detect time | ≤20 | 30-50 | ≥90 | Command & dispatch | Real-time | Road |
| 444 | Work-zone crash rate (per M VMT) | Crashes in work zones per million VMT | WZ crashes / WZ VMT(M) | ≤0.5 | 1-2 | ≥4 | Maintenance management | Monthly | Highway |
| 445 | Rail suicide/incident rate (per M train-km) | Unlawful track incidents per M train-km | Incidents / train-km(M) | ≤0.05 | 0.1-0.3 | ≥0.8 | Rail safety system | Monthly | Rail transit |
| 446 | Aviation fatal accident rate (per M flights) | Hull-loss accidents per M flights | Accidents / flights(M) | ≤0.1 | 0.2-0.5 | ≥1.0 | Aviation safety data | Annual | Civil aviation |
| 447 | Port safety incident rate (per M moves) | LTIF per million container moves | LTIF / moves(M) | ≤0.1 | 0.3-0.8 | ≥2.0 | Port safety system | Monthly | Port & waterway |
| 448 | Road safety audit coverage (%) | Projects with completed safety audit | Audited / total ×100% | ≥90% | 60-80% | ≤40% | Safety management | Annual | Road |
| 449 | Black-spot treatment progress (%) | Black spots treated vs identified | Treated / identified ×100% | ≥90% | 60-80% | ≤40% | Safety management | Annual | Road |
| 450 | ITS safety intervention benefit (%) | Crash reduction from ITS warning | (before − after)/before ×100% | ≥30% | 15-25% | ≤5% | Crash comparison | Annual | Road |
| 451 | Vulnerable-user KSI share (%) | VU share of total KSI | VU KSI / total KSI ×100% | ≤40% | 50-65% | ≥80% | Police crash stats | Annual | Active transportation |
| 452 | Emergency medical response time (min) | Time to on-scene for trauma | Arrival − call | ≤8 | 10-15 | ≥25 | EMS dispatch | Real-time | All modalities |
| 453 | Fatality rate per M tonnes freight | Freight fatalities per M tonnes moved | Freight deaths / tonnes(M) | ≤0.1 | 0.3-0.8 | ≥2.0 | Freight safety stats | Annual | Road freight |
| 454 | Pavement Condition Index (PCI) | Average pavement condition score 0-100 | Mean PCI over network | ≥85 | 70-80 | ≤55 | Pavement inspection | Annual | Highway |
| 455 | Bridge condition rating (NBI) | Average National Bridge Inventory rating | Mean NBI sufficiency | ≥80 | 60-75 | ≤50 | Bridge management | Annual | Highway |
| 456 | Intelligent street-light coverage (%) | Networked street lights vs total | Connected / total ×100% | ≥70% | 40-60% | ≤20% | Lighting management | Annual | Urban road |
| 457 | Traffic signal coordination coverage (%) | Coordinated signals vs total | Coordinated / total ×100% | ≥60% | 35-50% | ≤20% | Signal control system | Daily | Urban road |
| 458 | CCTV coverage of arterials (%) | Monitored arterial km vs total | Covered / total ×100% | ≥90% | 70-85% | ≤50% | Video surveillance | Annual | Urban road |
| 459 | VMS / dynamic message sign density | VMS per 10 km of expressway | VMS count / expressway km ×10 | ≥1.0 | 0.4-0.7 | ≤0.1 | Expressway management | Annual | Expressway |
| 460 | EV charging points per 100k pop | Public charge points per 100k residents | Points / pop ×100k | ≥800 | 300-600 | ≤100 | Charging platform | Annual | New-energy / Urban |
| 461 | Sensor network density (per km) | Traffic sensors per road km | Sensors / road km | ≥0.5 | 0.2-0.4 | ≤0.05 | Sensor management | Annual | Urban road |
| 462 | Tunnel SCADA coverage (%) | Tunnels with SCADA monitoring | Instrumented / total ×100% | ≥95% | 80-90% | ≤60% | Tunnel management | Annual | Highway |
| 463 | ITS backbone network availability (%) | Core communications uptime | Uptime / total ×100% | ≥99.9% | 99.5-99.8% | ≤99.0% | Network operations | Daily | All modalities |
| 464 | Edge-compute node coverage (%) | Intersections with edge nodes | Equipped / total ×100% | ≥50% | 20-40% | ≤5% | Edge computing platform | Annual | Urban road |
| 465 | Digital infrastructure redundancy (%) | Critical systems with N+1 redundancy | Redundant / critical ×100% | ≥95% | 80-90% | ≤60% | IT operations | Annual | All modalities |
| 466 | Asset condition index (%) | Share of assets in good condition | Good / total ×100% | ≥85% | 70-80% | ≤55% | Asset management | Annual | Highway |
| 467 | Roadside unit (RSU) coverage (%) | RSU along V2X corridors | Equipped km / total km ×100% | ≥60% | 25-45% | ≤10% | V2X platform | Annual | V2X |
| 468 | Fiber connectivity of intersections (%) | Signalised junctions on fiber | Fiber / total ×100% | ≥80% | 50-70% | ≤30% | Communications mgmt | Annual | Urban road |
| 469 | Resilience: recovery time (h) | Time to restore after disruption | Restore complete − event | ≤4 | 8-24 | ≥72 | Emergency management | Per event | All modalities |
| 470 | MaaS app adoption (%) | Residents using a MaaS app | Users / population ×100% | ≥30% | 10-20% | ≤3% | MaaS platform | Annual | MaaS |
| 471 | Real-time info coverage (%) | Stops/routes with real-time data | Served / total ×100% | ≥95% | 80-90% | ≤60% | GTFS-realtime | Daily | Public transport |
| 472 | Journey planner coverage (%) | Area with multimodal journey planning | Covered / total ×100% | ≥95% | 75-90% | ≤50% | Mobility platform | Annual | Mobility service |
| 473 | Contactless payment share (%) | Fares paid contactless | Contactless / total ×100% | ≥90% | 60-85% | ≤30% | Fare collection | Daily | Public transport |
| 474 | Ride-hailing trip share (%) | Ride-hailing of motorised trips | Ride-hail / total ×100% | ≤8% | 10-18% | ≥30% | Ride-hailing platform | Monthly | Ride-hailing |
| 475 | Demand-responsive transit coverage (%) | Area served by DRT | Served / total ×100% | ≥40% | 15-30% | ≤5% | DRT platform | Annual | Demand-responsive bus |
| 476 | Wheelchair-accessible vehicle share (%) | Accessible fleet vs total | Accessible / total ×100% | ≥100% | 80-95% | ≤50% | Fleet management | Annual | Public transport |
| 477 | Customer satisfaction (CSAT) | Passenger satisfaction score 1-5 | Mean survey score | ≥4.3 | 3.8-4.1 | ≤3.2 | Satisfaction survey | Quarterly | Public transport |
| 478 | First/last-mile connectivity (%) | Transit stops reachable by active mode 10 min | Connected / total ×100% | ≥90% | 70-85% | ≤50% | Mobility platform | Annual | Public transport |
| 479 | Trip planning accuracy (%) | Planned vs actual trip time | Accurate / total ×100% | ≥90% | 80-88% | ≤70% | MaaS platform | Daily | MaaS |
| 480 | Multimodal ticket integration (%) | Tickets valid across modes | Integrated / total ×100% | ≥80% | 40-65% | ≤20% | Fare clearing | Annual | Mobility service |
| 481 | Shared mobility fleet utilisation (%) | Active shared vehicles vs fleet | Active / total ×100% | ≥70% | 45-60% | ≤25% | Shared platform | Daily | Shared mobility |
| 482 | Taxi availability wait (min) | Average hail/booking wait | Σ wait / requests | ≤5 | 8-15 | ≥30 | Taxi platform | Daily | Taxi |
| 483 | Info accessibility compliance (%) | Conformance to WCAG 2.1 AA | Conformant / total ×100% | ≥100% | 80-95% | ≤60% | Accessibility audit | Annual | Mobility service |
| 484 | Service disruption comms time (min) | Time to notify passengers of disruption | Notify − detect | ≤3 | 5-10 | ≥20 | Ops monitoring | Real-time | Public transport |
| 485 | Congestion cost (% of GDP) | Delay cost as share of GDP | Delay cost / GDP ×100% | ≤1.0% | 1.5-2.5% | ≥4.0% | HPMS / economics | Annual | Urban road |
| 486 | Vehicle operating cost ($/veh-km) | Average user cost per veh-km | Total cost / VKT | ≤0.25 | 0.30-0.45 | ≥0.60 | Transport accounts | Annual | Road |
| 487 | Transit farebox recovery (%) | Fare revenue vs operating cost | Fare / operating cost ×100% | ≥80% | 40-60% | ≤20% | Finance system | Annual | Public transport |
| 488 | Labour productivity (PT rev/FTE) | PT revenue per full-time equiv | Revenue / FTE | ≥150k | 80-120k | ≤40k | Finance system | Annual | Public transport |
| 489 | PPP maturity index | Readiness for PPP procurement | Composite 0-100 | ≥75 | 50-65 | ≤30 | PPP info platform | Annual | All modalities |
| 490 | Capital project on-budget (%) | Projects delivered within budget | On-budget / total ×100% | ≥85% | 65-80% | ≤50% | Project management | Annual | All modalities |
| 491 | Asset renewal backlog ($/capita) | Deferred maintenance per resident | Backlog / population | ≤50 | 80-150 | ≥300 | Asset management | Annual | Highway |
| 492 | Freight logistics cost (% GDP) | Total logistics cost as share GDP | Logistics cost / GDP ×100% | ≤8% | 10-13% | ≥16% | Logistics accounts | Annual | Logistics |
| 493 | Road user cost savings ($/yr) | Annual savings from ITS | Σ savings | ≥50M | 10-30M | ≤1M | Benefit-cost model | Annual | Road |
| 494 | Digital service ROI (%) | Return on digital investments | (benefit − cost)/cost ×100% | ≥25% | 10-20% | ≤0% | Finance system | Annual | All modalities |
| 495 | Parking revenue per space ($/yr) | Annual parking revenue per space | Revenue / spaces | ≥3k | 1.5-2.5k | ≤0.5k | Parking platform | Annual | Urban parking |
| 496 | Non-fare revenue share (%) | Non-fare of operator revenue | Non-fare / total ×100% | ≥25% | 10-18% | ≤5% | Finance system | Annual | Public transport |
| 497 | Procurement lead time (days) | Avg time to award contract | Award − tender | ≤120 | 180-300 | ≥540 | Procurement system | Annual | All modalities |
| 498 | Cost per VMT maintained ($) | Maintenance spend per VMT | Spend / VMT | ≤0.02 | 0.03-0.05 | ≥0.08 | Maintenance mgmt | Annual | Highway |
| 499 | Economic accessibility (jobs within 45 min) | Jobs reachable by PT in 45 min | Mean reachable jobs | ≥80% | 50-70% | ≤30% | Accessibility model | Annual | Urban traffic |
| 500 | Transport CO2 per capita (t) | Annual per-capita transport CO2 | Total / population | ≤1.5 | 2.5-4.0 | ≥6.0 | Emissions inventory | Annual | All modalities |
| 501 | EV share of new vehicle sales (%) | New sales that are electric | EV sales / total ×100% | ≥50% | 15-30% | ≤5% | Vehicle registration | Annual | New-energy / Urban |
| 502 | Bus fleet electrification (%) | Electric buses vs total | e-bus / total ×100% | ≥80% | 30-60% | ≤10% | Fleet management | Annual | Public bus |
| 503 | Charging energy renewable share (%) | Renewable share of charging | Renewable / total ×100% | ≥60% | 20-40% | ≤5% | Energy platform | Annual | New-energy |
| 504 | Modal shift to active (%) | Walk+cycle share of trips | Active / total ×100% | ≥35% | 15-25% | ≤8% | Travel survey | Annual | Active transportation |
| 505 | Average passenger occupancy (PT) | Passengers per PT vehicle | Passengers / vehicles | ≥25 | 15-22 | ≤8 | AVL / AFC | Daily | Public transport |
| 506 | Well-to-wheel intensity (gCO2/pkm) | PT gCO2 per passenger-km | Emissions / pkm | ≤40 | 60-90 | ≥140 | Emissions model | Annual | Public transport |
| 507 | Freight empty-running rate (%) | Empty truck km vs total | Empty / total ×100% | ≤20% | 28-38% | ≥50% | Freight GPS | Monthly | Road freight |
| 508 | Low-carbon freight share (%) | Low-carbon modes of ton-km | Low-carbon / total ×100% | ≥40% | 20-35% | ≤10% | Freight stats | Annual | Logistics |
| 509 | Particulate matter (PM2.5) from transport | Transport-attributable PM2.5 | Model estimate | ≤10 | 15-25 | ≥40 | Air quality model | Annual | Urban traffic |
| 510 | Noise-exceedance population | Residents exposed >55 dB | Exposed / total ×100% | ≤10% | 20-35% | ≥50% | Noise model | Annual | Urban road |
| 511 | Carbon-neutral target year | Declared net-zero year | Year value | ≤2035 | 2040-2050 | >=2060 | Policy records | Annual | All modalities |
| 512 | Green procurement share (%) | Low-carbon in procurement | Green / total ×100% | ≥50% | 20-40% | ≤10% | Procurement system | Annual | All modalities |
| 513 | Idle-reduction benefit (%) | Emissions cut from idle control | (before − after)/before ×100% | ≥15% | 8-12% | ≤3% | Fleet telematics | Monthly | Road freight |
| 514 | Shared mobility carbon saving (tCO2/yr) | Annual CO2 avoided by sharing | Model estimate | ≥20k | 5-15k | ≤1k | Shared platform | Annual | Shared mobility |
| 515 | Renewable H2 refuelling sites | Sites for fuel-cell vehicles | Count | ≥20 | 5-15 | ≤1 | Energy platform | Annual | New-energy |
| 516 | Building energy (depots) | Energy use of facilities | kWh / depot | ≤200k | 300-500k | >=800k | Facility management | Annual | Public transport |
| 517 | Recycling rate of infrastructure (%) | Reclaimed asphalt etc. | Recycled / total ×100% | ≥40% | 20-35% | ≤10% | Maintenance mgmt | Annual | Highway |
| 518 | Eco-driving adoption (%) | Fleet with eco-driving program | Adopted / total ×100% | ≥70% | 30-55% | ≤15% | Fleet management | Annual | Road freight |
| 519 | Sustainable aviation fuel share (%) | SAF of jet fuel | SAF / total ×100% | ≥10% | 2-5% | ≤0.5% | Airline reports | Annual | Civil aviation |
| 520 | Open-data portal maturity | Maturity of transport open data | Composite 0-100 | ≥80 | 55-70 | ≤30 | Open-data platform | Annual | All modalities |
| 521 | Data sharing agreement coverage (%) | Agencies with data MOUs | Covered / total ×100% | ≥90% | 60-80% | ≤30% | Data governance | Annual | All modalities |
| 522 | Real-time data latency (s) | End-to-end latency of RT feeds | Detect − publish | ≤2 | 5-10 | ≥30 | Stream platform | Real-time | All modalities |
| 523 | Digital-twin coverage (%) | Network with digital twin | Covered / total ×100% | ≥50% | 20-40% | ≤10% | Digital-twin platform | Annual | All modalities |
| 524 | AI model accuracy (%) | Mean accuracy of deployed models | Correct / total ×100% | ≥90% | 80-88% | ≤65% | AI model platform | Daily | All modalities |
| 525 | Data quality score (%) | Conformance to DQ rules | Pass / total ×100% | ≥95% | 85-92% | ≤70% | Data quality platform | Daily | All modalities |
| 526 | Cloud utilisation (%) | Workloads on cloud | Cloud / total ×100% | ≥80% | 50-70% | ≤30% | Cloud platform | Annual | All modalities |
| 527 | API availability (%) | Public API uptime | Uptime / total ×100% | ≥99.9% | 99.5-99.8% | ≤99.0% | API gateway | Daily | All modalities |
| 528 | Incident detection MTTR (min) | Mean time to resolve data incidents | Resolve − detect | ≤30 | 60-120 | ≥300 | Data ops | Daily | All modalities |
| 529 | Model drift alert rate (%) | Models with drift monitoring | Monitored / total ×100% | ≥90% | 60-80% | ≤40% | AI platform | Daily | All modalities |
| 530 | Data catalog coverage (%) | Catalogued datasets vs total | Catalogued / total ×100% | ≥85% | 55-75% | ≤30% | Data catalog | Annual | All modalities |
| 531 | Privacy impact assessments (%) | Systems with DPIA | Assessed / total ×100% | ≥95% | 70-85% | ≤50% | Compliance system | Annual | All modalities |
| 532 | Automated decision rate (%) | Decisions automated vs manual | Auto / total ×100% | ≥40% | 15-30% | ≤5% | Decision support | Annual | All modalities |
| 533 | Simulation model coverage (%) | Corridors with calibrated models | Covered / total ×100% | ≥60% | 30-50% | ≤15% | Modelling platform | Annual | Urban road |
| 534 | Data literacy training (%) | Staff with data training | Trained / total ×100% | ≥80% | 50-70% | ≤30% | Training system | Annual | All modalities |
| 535 | ISO 37120 compliance | Conformance to city indicators | Conformant / total ×100% | ≥95% | 70-85% | ≤40% | Standards audit | Annual | Urban traffic |
| 536 | Strategy & KPI framework | Documented digital strategy exists | Binary | Yes | Partial | No | Governance records | Annual | All modalities |
| 537 | Cybersecurity maturity (NIST CSF) | CSF maturity score 1-4 | Mean score | ≥3.5 | 2.5-3.0 | ≤1.5 | Security audit | Annual | All modalities |
| 538 | Staff digital skills (%) | Staff with digital competencies | Skilled / total ×100% | ≥75% | 50-65% | ≤30% | HR system | Annual | All modalities |
| 539 | Innovation pipeline count | Active pilot/innovation projects | Count | ≥20 | 8-15 | ≤3 | Innovation mgmt | Annual | All modalities |
| 540 | Procurement transparency (%) | Tenders published openly | Published / total ×100% | ≥95% | 75-90% | ≤50% | Procurement system | Annual | All modalities |
| 541 | Stakeholder satisfaction | Agency stakeholder CSAT | Mean 1-5 | ≥4.2 | 3.6-4.0 | ≤3.0 | Stakeholder survey | Annual | All modalities |
| 542 | Risk register coverage (%) | Assets with risk assessment | Assessed / total ×100% | ≥90% | 65-80% | ≤40% | Risk register | Annual | All modalities |
| 543 | Business continuity tested (%) | Plans tested annually | Tested / total ×100% | ≥100% | 60-85% | ≤30% | BCM system | Annual | All modalities |
| 544 | Ethics/AI governance policy | Documented AI ethics policy | Binary | Yes | Partial | No | Governance records | Annual | All modalities |
| 545 | Performance reporting frequency | KPI reporting cadence | Per week / month / quarter | Weekly | Monthly | Quarterly | Performance system | Annual | All modalities |
| 546 | Inter-agency data MOUs | Signed data-sharing MOUs | Count | ≥10 | 4-8 | ≤1 | Governance records | Annual | All modalities |
| 547 | Citizen participation rate (%) | Public in consultations | Participated / reached ×100% | ≥15% | 5-10% | ≤1% | Engagement platform | Annual | All modalities |
| 548 | Standardisation adoption (%) | Use of int'l standards (ISO/ETSI) | Adopted / total ×100% | ≥80% | 50-70% | ≤30% | Standards mgmt | Annual | All modalities |
| 549 | Logistics Performance Index rank | World Bank LPI rank | Rank 1-160 | ≤20 | 40-80 | ≥130 | World Bank LPI | Biennial | Logistics |
| 550 | Freight ton-km growth (%) | Annual ton-km change | (curr − prev)/prev ×100% | ≥4% | 1-3% | ≤0% | Freight stats | Annual | Logistics |
| 551 | Average freight dwell time (h) | Terminal dwell of containers | Σ dwell / units | ≤24 | 36-60 | ≥96 | Terminal system | Daily | Port & waterway |
| 552 | Empty container repositioning (%) | Empty moves vs total | Empty / total ×100% | ≤20% | 28-38% | ≥50% | Container system | Monthly | Port & waterway |
| 553 | Warehouse automation rate (%) | Automated warehouses vs total | Automated / total ×100% | ≥40% | 15-30% | ≤5% | WMS | Annual | Logistics warehousing |
| 554 | Last-mile cost ($/parcel) | Average last-mile delivery cost | Last-mile cost / parcels | ≤2 | 3-5 | ≥8 | Parcel platform | Monthly | Parcel/Express |
| 555 | Parcel on-time delivery (%) | Parcels delivered on time | On-time / total ×100% | ≥98% | 92-96% | ≤85% | Parcel platform | Daily | Parcel/Express |
| 556 | Cross-border clearance time (h) | Time to clear customs | Exit − entry | ≤6 | 12-24 | ≥72 | Customs Single Window | Per shipment | Cross-border |
| 557 | Cold-chain breach rate (%) | Temp excursions in cold chain | Breaches / total ×100% | ≤0.5% | 1-3% | ≥8% | Cold-chain IoT | Daily | Cold-chain |
| 558 | Freight visibility (%) | Shipments with real-time track | Tracked / total ×100% | ≥90% | 65-85% | ≤40% | Tracking platform | Daily | Logistics |
| 559 | Multimodal share of freight (%) | Multimodal of ton-km | Multimodal / total ×100% | ≥35% | 15-30% | ≤8% | Multimodal platform | Annual | Multimodal |
| 560 | Truck load factor (%) | Average laden weight vs capacity | Laden / capacity ×100% | ≥75% | 55-70% | ≤40% | Weighbridge | Monthly | Road freight |
| 561 | Rail freight mode share (%) | Rail of land freight ton-km | Rail / land ×100% | ≥30% | 15-25% | ≤8% | Railway stats | Annual | Railway |
| 562 | Hub throughput (TEU/yr) | Annual hub container throughput | Σ throughput | ≥5M | 1-3M | ≤0.3M | Hub system | Annual | Integrated hub |
| 563 | Warehouse occupancy rate (%) | Occupied vs total warehouse | Occupied / total ×100% | ≤85% | 88-95% | ≥99% | WMS | Monthly | Logistics warehousing |
| 564 | CO2 per ton-km (freight, g) | Freight gCO2 per ton-km | Emissions / ton-km | ≤30 | 50-80 | ≥120 | Emissions model | Annual | Logistics |
| 565 | Multimodal journey share (%) | Trips using ≥2 modes | Multi / total ×100% | ≥25% | 10-20% | ≤5% | Mobility platform | Annual | Multimodal |
| 566 | Hub transfer satisfaction | Transfer experience CSAT 1-5 | Mean score | ≥4.3 | 3.7-4.0 | ≤3.0 | Hub survey | Quarterly | Integrated hub |
| 567 | Urban-rural access gap | Rural vs urban service frequency ratio | Rural freq / urban freq | ≥0.7 | 0.4-0.6 | ≤0.2 | Service registry | Annual | Urban-rural |
| 568 | Cross-border corridor time (h) | Transit time across borders | Σ border delay | ≤2 | 4-10 | ≥24 | Customs Single Window | Per crossing | Cross-border |
| 569 | Emergency evacuation clearance (h) | Time to evacuate corridor | Clear − alert | ≤2 | 4-8 | ≥16 | Emergency management | Per event | All modalities |
| 570 | New-tech adoption index | Adoption of AV/UTM/UAM | Composite 0-100 | ≥60 | 30-50 | ≤10 | Innovation mgmt | Annual | Autonomous driving |

## Appendix A: 15 Transport Modalities

| ID | Modality | English | Coverage (KPI #) |
|------|----------|------|----------|
| M01 | urban road | Urban Road | 1-25, 30-31, 86-95, 96-105, 136-155, 167-172, 177-195 |
| M02 | expressway | Expressway | 26-40, 90, 136-155, 196-200, 349 |
| M03 | public bus | Public Bus | 41-47, 108-109, 177-186, 215-217 |
| M04 | rail transit | Rail Transit | 48-52, 106-107, 110, 156-159, 183-184, 216-219, 224 |
| M05 | BRT | Bus Rapid Transit | 53 |
| M06 | taxi / ride-hailing | Taxi/Ride-hailing | 192-194 |
| M07 | shared mobility | Shared Mobility | 80-81, 195, 259 |
| M08 | active transportation | Active Transportation | 82-85, 259 |
| M09 | port & waterway | Port/Waterway | 59-65, 111-113, 160-162, 220, 257, 265 |
| M10 | civil aviation | Civil Aviation | 66-74, 114-116, 163-165, 221, 248, 258 |
| M11 | railway | Railway | 75-79, 166, 247, 375-376 |
| M12 | logistics / parcel | Logistics/Express | 173-176, 341-379 |
| M13 | multimodal | Multimodal Transport | 176, 345-346, 380-384 |
| M14 | integrated hub | Integrated Transport Hub | 54-58, 385-389 |
| M15 | V2X / autonomous driving | V2X/Autonomous Driving | 101-102, 152-153, 402-404 |

---

## Appendix B: 12 Business Chains

| ID | Business Chain | English | Description |
|------|-----------|------|------|
| C01 | transport planning | Transport Planning | road network / line network / hub planning, transport etc. |
| C02 | transport design | Transport Design | earth build / machine electric / system design |
| C03 | construction | Construction | construction management, quality safety management |
| C04 | traffic operation | Traffic Operation | road network / bus / rail / operate dispatch |
| C05 | mobility service | Mobility Service | information service, MaaS |
| C06 | maintenance | Maintenance | road / vehicle / equipment |
| C07 | safety management | Safety Management | crash, emergency, cybersecurity |
| C08 | enforcement | Enforcement | transport enforcement, over-limit governance, market supervision |
| C09 | asset management | Asset Management | / data assets manage |
| C10 | finance & revenue | Finance & Revenue | / / / compute |
| C11 | R&D & innovation | R&D & Innovation | technology, standard, application |
| C12 | governance | Governance | institution / system / institution / system / talent / |

---

## Appendix C: Data Source Abbreviations

| Abbr. | Full Name | Notes |
|------|------|------|
| vehicle GP S | Floating Car Data (FCD)/ GP S | taxi / ride-hailing / APP etc. data |
| line detect | Inductive Loop Detector | or line vehicle detect |
| mouth | Video ANPR/Checkpoint | electric / mouth license-plate recognition |
| / detect | Microwave/Radar Sensor | vehicle / m |
| ETC | ETC Gantry | expressway ETC system |
| AFC | Automatic Fare Collection | rail transit automatic system |
| IC | Smart Card (Transit) | bus / transport |
| TOS | Terminal Operating System | container as system |
| AIS | Automatic Identification System | vessel automatic identify system |
| ADS-B | Automatic Dependent Surveillance-Broadcast | automatic |
| V2X | Vehicle-to-Everything | vehicle network / V2X communications |
| IoT | Internet of Things | IoT network |
| SOC | Security Operations Center | safety operation in |
| WMS | Warehouse Management System | warehousing manage system |
| TMS | Transportation Management System | transport manage system |

---

> **Compilation note**: This library draws on ISO 37120 (city indicators), the European ITS Directive 2010/40/EU, FHWA HPMS, the World Bank Logistics Performance Index (LPI), ITF/ECMT benchmarking, OECD transport statistics, and benchmark data from leading international cities (Singapore, Tokyo, London, New York, Amsterdam, Seoul). Benchmarks (leading/median/lagging) reflect international best practice and peer-city experience.

> **Total**: 411 core KPIs (re-baselined to global benchmarks) + 159 international benchmark KPIs (Section XI) = 570 KPIs
