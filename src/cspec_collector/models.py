from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class FlexibleModel(BaseModel):
    model_config = ConfigDict(extra="allow")


class CriterionRecord(FlexibleModel):
    gene_symbol: str | None = None
    hgnc_id: str | None = None
    cspec_id: str
    version: str | None = None
    ruleset_id: str | None = None
    criterion_code: str | None = None
    criterion_label: str | None = None
    criterion_description: str | None = None
    strength: str | None = None
    strength_descriptor: str | None = None
    applicability: str | None = None
    diseases: list[Any] = Field(default_factory=list)
    modes_of_inheritance: list[Any] = Field(default_factory=list)
    source_api_url: str
    fetched_at: str


class DocumentRecord(FlexibleModel):
    cspec_id: str
    title: str | None = None
    vcep: str | None = None
    version: str | None = None
    document_status: str
    status_history: list[Any] = Field(default_factory=list)
    release_date: str | None = None
    modified_at: str | None = None
    genes: list[dict[str, Any]] = Field(default_factory=list)
    diseases: list[Any] = Field(default_factory=list)
    modes_of_inheritance: list[Any] = Field(default_factory=list)
    legacy_replaced: bool | None = None
    legacy_fully_superseded: bool | None = None
    source_api_url: str
    source_ui_url: str
    fetched_at: str
    content_sha256: str
    parser_version: str
