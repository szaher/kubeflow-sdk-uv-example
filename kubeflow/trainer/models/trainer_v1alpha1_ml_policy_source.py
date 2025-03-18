# coding: utf-8

"""
    Kubeflow Trainer OpenAPI Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: unversioned
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.trainer_v1alpha1_mpiml_policy_source import TrainerV1alpha1MPIMLPolicySource
from kubeflow.trainer.models.trainer_v1alpha1_torch_ml_policy_source import TrainerV1alpha1TorchMLPolicySource
from typing import Optional, Set
from typing_extensions import Self

class TrainerV1alpha1MLPolicySource(BaseModel):
    """
    MLPolicySource represents the runtime-specific configuration for various technologies. One of the following specs can be set.
    """ # noqa: E501
    mpi: Optional[TrainerV1alpha1MPIMLPolicySource] = Field(default=None, description="Configuration for the MPI Runtime.")
    torch: Optional[TrainerV1alpha1TorchMLPolicySource] = Field(default=None, description="Configuration for the PyTorch runtime.")
    __properties: ClassVar[List[str]] = ["mpi", "torch"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TrainerV1alpha1MLPolicySource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of mpi
        if self.mpi:
            _dict['mpi'] = self.mpi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of torch
        if self.torch:
            _dict['torch'] = self.torch.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrainerV1alpha1MLPolicySource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mpi": TrainerV1alpha1MPIMLPolicySource.from_dict(obj["mpi"]) if obj.get("mpi") is not None else None,
            "torch": TrainerV1alpha1TorchMLPolicySource.from_dict(obj["torch"]) if obj.get("torch") is not None else None
        })
        return _obj


