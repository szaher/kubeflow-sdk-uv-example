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
from kubeflow.trainer.models.io_k8s_api_core_v1_aws_elastic_block_store_volume_source import IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_azure_disk_volume_source import IoK8sApiCoreV1AzureDiskVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_azure_file_persistent_volume_source import IoK8sApiCoreV1AzureFilePersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_ceph_fs_persistent_volume_source import IoK8sApiCoreV1CephFSPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_cinder_persistent_volume_source import IoK8sApiCoreV1CinderPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_csi_persistent_volume_source import IoK8sApiCoreV1CSIPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_fc_volume_source import IoK8sApiCoreV1FCVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_flex_persistent_volume_source import IoK8sApiCoreV1FlexPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_flocker_volume_source import IoK8sApiCoreV1FlockerVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_gce_persistent_disk_volume_source import IoK8sApiCoreV1GCEPersistentDiskVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_glusterfs_persistent_volume_source import IoK8sApiCoreV1GlusterfsPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_host_path_volume_source import IoK8sApiCoreV1HostPathVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_iscsi_persistent_volume_source import IoK8sApiCoreV1ISCSIPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_local_volume_source import IoK8sApiCoreV1LocalVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_nfs_volume_source import IoK8sApiCoreV1NFSVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_photon_persistent_disk_volume_source import IoK8sApiCoreV1PhotonPersistentDiskVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_portworx_volume_source import IoK8sApiCoreV1PortworxVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_quobyte_volume_source import IoK8sApiCoreV1QuobyteVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_rbd_persistent_volume_source import IoK8sApiCoreV1RBDPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_scale_io_persistent_volume_source import IoK8sApiCoreV1ScaleIOPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_storage_os_persistent_volume_source import IoK8sApiCoreV1StorageOSPersistentVolumeSource
from kubeflow.trainer.models.io_k8s_api_core_v1_vsphere_virtual_disk_volume_source import IoK8sApiCoreV1VsphereVirtualDiskVolumeSource
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1PersistentVolumeSource(BaseModel):
    """
    PersistentVolumeSource is similar to VolumeSource but meant for the administrator who creates PVs. Exactly one of its members must be set.
    """ # noqa: E501
    aws_elastic_block_store: Optional[IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource] = Field(default=None, description="awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Deprecated: AWSElasticBlockStore is deprecated. All operations for the in-tree awsElasticBlockStore type are redirected to the ebs.csi.aws.com CSI driver. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore", alias="awsElasticBlockStore")
    azure_disk: Optional[IoK8sApiCoreV1AzureDiskVolumeSource] = Field(default=None, description="azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. Deprecated: AzureDisk is deprecated. All operations for the in-tree azureDisk type are redirected to the disk.csi.azure.com CSI driver.", alias="azureDisk")
    azure_file: Optional[IoK8sApiCoreV1AzureFilePersistentVolumeSource] = Field(default=None, description="azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver.", alias="azureFile")
    cephfs: Optional[IoK8sApiCoreV1CephFSPersistentVolumeSource] = Field(default=None, description="cephFS represents a Ceph FS mount on the host that shares a pod's lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported.")
    cinder: Optional[IoK8sApiCoreV1CinderPersistentVolumeSource] = Field(default=None, description="cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: https://examples.k8s.io/mysql-cinder-pd/README.md")
    csi: Optional[IoK8sApiCoreV1CSIPersistentVolumeSource] = Field(default=None, description="csi represents storage that is handled by an external CSI driver.")
    fc: Optional[IoK8sApiCoreV1FCVolumeSource] = Field(default=None, description="fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.")
    flex_volume: Optional[IoK8sApiCoreV1FlexPersistentVolumeSource] = Field(default=None, description="flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead.", alias="flexVolume")
    flocker: Optional[IoK8sApiCoreV1FlockerVolumeSource] = Field(default=None, description="flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported.")
    gce_persistent_disk: Optional[IoK8sApiCoreV1GCEPersistentDiskVolumeSource] = Field(default=None, description="gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk", alias="gcePersistentDisk")
    glusterfs: Optional[IoK8sApiCoreV1GlusterfsPersistentVolumeSource] = Field(default=None, description="glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported. More info: https://examples.k8s.io/volumes/glusterfs/README.md")
    host_path: Optional[IoK8sApiCoreV1HostPathVolumeSource] = Field(default=None, description="hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath", alias="hostPath")
    iscsi: Optional[IoK8sApiCoreV1ISCSIPersistentVolumeSource] = Field(default=None, description="iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.")
    local: Optional[IoK8sApiCoreV1LocalVolumeSource] = Field(default=None, description="local represents directly-attached storage with node affinity")
    nfs: Optional[IoK8sApiCoreV1NFSVolumeSource] = Field(default=None, description="nfs represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs")
    photon_persistent_disk: Optional[IoK8sApiCoreV1PhotonPersistentDiskVolumeSource] = Field(default=None, description="photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine. Deprecated: PhotonPersistentDisk is deprecated and the in-tree photonPersistentDisk type is no longer supported.", alias="photonPersistentDisk")
    portworx_volume: Optional[IoK8sApiCoreV1PortworxVolumeSource] = Field(default=None, description="portworxVolume represents a portworx volume attached and mounted on kubelets host machine. Deprecated: PortworxVolume is deprecated. All operations for the in-tree portworxVolume type are redirected to the pxd.portworx.com CSI driver when the CSIMigrationPortworx feature-gate is on.", alias="portworxVolume")
    quobyte: Optional[IoK8sApiCoreV1QuobyteVolumeSource] = Field(default=None, description="quobyte represents a Quobyte mount on the host that shares a pod's lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported.")
    rbd: Optional[IoK8sApiCoreV1RBDPersistentVolumeSource] = Field(default=None, description="rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported. More info: https://examples.k8s.io/volumes/rbd/README.md")
    scale_io: Optional[IoK8sApiCoreV1ScaleIOPersistentVolumeSource] = Field(default=None, description="scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported.", alias="scaleIO")
    storageos: Optional[IoK8sApiCoreV1StorageOSPersistentVolumeSource] = Field(default=None, description="storageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported. More info: https://examples.k8s.io/volumes/storageos/README.md")
    vsphere_volume: Optional[IoK8sApiCoreV1VsphereVirtualDiskVolumeSource] = Field(default=None, description="vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver.", alias="vsphereVolume")
    __properties: ClassVar[List[str]] = ["awsElasticBlockStore", "azureDisk", "azureFile", "cephfs", "cinder", "csi", "fc", "flexVolume", "flocker", "gcePersistentDisk", "glusterfs", "hostPath", "iscsi", "local", "nfs", "photonPersistentDisk", "portworxVolume", "quobyte", "rbd", "scaleIO", "storageos", "vsphereVolume"]

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
        """Create an instance of IoK8sApiCoreV1PersistentVolumeSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aws_elastic_block_store
        if self.aws_elastic_block_store:
            _dict['awsElasticBlockStore'] = self.aws_elastic_block_store.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_disk
        if self.azure_disk:
            _dict['azureDisk'] = self.azure_disk.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_file
        if self.azure_file:
            _dict['azureFile'] = self.azure_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cephfs
        if self.cephfs:
            _dict['cephfs'] = self.cephfs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cinder
        if self.cinder:
            _dict['cinder'] = self.cinder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of csi
        if self.csi:
            _dict['csi'] = self.csi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fc
        if self.fc:
            _dict['fc'] = self.fc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flex_volume
        if self.flex_volume:
            _dict['flexVolume'] = self.flex_volume.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flocker
        if self.flocker:
            _dict['flocker'] = self.flocker.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gce_persistent_disk
        if self.gce_persistent_disk:
            _dict['gcePersistentDisk'] = self.gce_persistent_disk.to_dict()
        # override the default output from pydantic by calling `to_dict()` of glusterfs
        if self.glusterfs:
            _dict['glusterfs'] = self.glusterfs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of host_path
        if self.host_path:
            _dict['hostPath'] = self.host_path.to_dict()
        # override the default output from pydantic by calling `to_dict()` of iscsi
        if self.iscsi:
            _dict['iscsi'] = self.iscsi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of local
        if self.local:
            _dict['local'] = self.local.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nfs
        if self.nfs:
            _dict['nfs'] = self.nfs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of photon_persistent_disk
        if self.photon_persistent_disk:
            _dict['photonPersistentDisk'] = self.photon_persistent_disk.to_dict()
        # override the default output from pydantic by calling `to_dict()` of portworx_volume
        if self.portworx_volume:
            _dict['portworxVolume'] = self.portworx_volume.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quobyte
        if self.quobyte:
            _dict['quobyte'] = self.quobyte.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rbd
        if self.rbd:
            _dict['rbd'] = self.rbd.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scale_io
        if self.scale_io:
            _dict['scaleIO'] = self.scale_io.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storageos
        if self.storageos:
            _dict['storageos'] = self.storageos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vsphere_volume
        if self.vsphere_volume:
            _dict['vsphereVolume'] = self.vsphere_volume.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1PersistentVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "awsElasticBlockStore": IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource.from_dict(obj["awsElasticBlockStore"]) if obj.get("awsElasticBlockStore") is not None else None,
            "azureDisk": IoK8sApiCoreV1AzureDiskVolumeSource.from_dict(obj["azureDisk"]) if obj.get("azureDisk") is not None else None,
            "azureFile": IoK8sApiCoreV1AzureFilePersistentVolumeSource.from_dict(obj["azureFile"]) if obj.get("azureFile") is not None else None,
            "cephfs": IoK8sApiCoreV1CephFSPersistentVolumeSource.from_dict(obj["cephfs"]) if obj.get("cephfs") is not None else None,
            "cinder": IoK8sApiCoreV1CinderPersistentVolumeSource.from_dict(obj["cinder"]) if obj.get("cinder") is not None else None,
            "csi": IoK8sApiCoreV1CSIPersistentVolumeSource.from_dict(obj["csi"]) if obj.get("csi") is not None else None,
            "fc": IoK8sApiCoreV1FCVolumeSource.from_dict(obj["fc"]) if obj.get("fc") is not None else None,
            "flexVolume": IoK8sApiCoreV1FlexPersistentVolumeSource.from_dict(obj["flexVolume"]) if obj.get("flexVolume") is not None else None,
            "flocker": IoK8sApiCoreV1FlockerVolumeSource.from_dict(obj["flocker"]) if obj.get("flocker") is not None else None,
            "gcePersistentDisk": IoK8sApiCoreV1GCEPersistentDiskVolumeSource.from_dict(obj["gcePersistentDisk"]) if obj.get("gcePersistentDisk") is not None else None,
            "glusterfs": IoK8sApiCoreV1GlusterfsPersistentVolumeSource.from_dict(obj["glusterfs"]) if obj.get("glusterfs") is not None else None,
            "hostPath": IoK8sApiCoreV1HostPathVolumeSource.from_dict(obj["hostPath"]) if obj.get("hostPath") is not None else None,
            "iscsi": IoK8sApiCoreV1ISCSIPersistentVolumeSource.from_dict(obj["iscsi"]) if obj.get("iscsi") is not None else None,
            "local": IoK8sApiCoreV1LocalVolumeSource.from_dict(obj["local"]) if obj.get("local") is not None else None,
            "nfs": IoK8sApiCoreV1NFSVolumeSource.from_dict(obj["nfs"]) if obj.get("nfs") is not None else None,
            "photonPersistentDisk": IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.from_dict(obj["photonPersistentDisk"]) if obj.get("photonPersistentDisk") is not None else None,
            "portworxVolume": IoK8sApiCoreV1PortworxVolumeSource.from_dict(obj["portworxVolume"]) if obj.get("portworxVolume") is not None else None,
            "quobyte": IoK8sApiCoreV1QuobyteVolumeSource.from_dict(obj["quobyte"]) if obj.get("quobyte") is not None else None,
            "rbd": IoK8sApiCoreV1RBDPersistentVolumeSource.from_dict(obj["rbd"]) if obj.get("rbd") is not None else None,
            "scaleIO": IoK8sApiCoreV1ScaleIOPersistentVolumeSource.from_dict(obj["scaleIO"]) if obj.get("scaleIO") is not None else None,
            "storageos": IoK8sApiCoreV1StorageOSPersistentVolumeSource.from_dict(obj["storageos"]) if obj.get("storageos") is not None else None,
            "vsphereVolume": IoK8sApiCoreV1VsphereVirtualDiskVolumeSource.from_dict(obj["vsphereVolume"]) if obj.get("vsphereVolume") is not None else None
        })
        return _obj


