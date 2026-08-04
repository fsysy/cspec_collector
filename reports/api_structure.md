# CSpec API structure

Observed from the live API.

- List path: `/cspec/SequenceVariantInterpretation/id`
- Valid `detail` values: `nold`, `low`, `med`, `high`
- JSON-LD path: `/cspec/api/SequenceVariantInterpretation/id/{cspec_id}`
- Document fields: `@id`, `label`, `version`, `affiliation`, `currentStatus`, `ruleSets`
- Genes: `ruleSets[].genes[]`; diseases: `genes[].diseases[]`; inheritance: `diseases[].modeOfInheritance[]`
- Criteria: `ruleSets[].criteriaCodes[]`; strengths: `criteriaCodes[].evidenceStrengths[]`
- Status history and legacy flags are available in the high-detail list record under `entContent` when supplied.

Sample IDs: GN001, GN002, GN003
