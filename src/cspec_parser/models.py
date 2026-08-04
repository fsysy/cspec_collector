from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class RuleRecord(BaseModel):
    model_config = ConfigDict(extra="allow")
    rule_id: str
    cspec_id: str
    gene: str | None = None
    hgnc_id: str | None = None
    criterion: str
    criterion_raw: str | None = None
    direction: str
    applicable: bool | None = None
    strength: str | None = None
    allowed_strengths: list[str] = Field(default_factory=list)
    default_strength: str | None = None
    thresholds: list[dict[str, Any]] = Field(default_factory=list)
    conditions: list[dict[str, Any]] = Field(default_factory=list)
    exclusions: list[dict[str, Any]] = Field(default_factory=list)
    variant_types: list[str] = Field(default_factory=list)
    regions: list[dict[str, Any]] = Field(default_factory=list)
    transcripts: list[str] = Field(default_factory=list)
    diseases: list[Any] = Field(default_factory=list)
    modes_of_inheritance: list[Any] = Field(default_factory=list)
    summary: str = ""
    rule_text: str = ""
    notes: list[str] = Field(default_factory=list)
    references: list[Any] = Field(default_factory=list)
    source_path: str = ""
    source_paths: list[str] = Field(default_factory=list)
    source_api_url: str = ""
    source_ui_url: str = ""
    document_version: str | None = None
    document_status: str | None = None
    release_date: str | None = None
    extraction_confidence: str = "high"
    requires_manual_review: bool = False

