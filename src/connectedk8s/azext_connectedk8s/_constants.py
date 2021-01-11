# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


# pylint: disable=line-too-long

Distribution_Enum_Values = ["auto", "generic", "openshift", "rancher_rke", "kind", "k3s", "minikube", "gke", "eks", "aks", "aks_hci", "capz", "aks_engine", "tkg"]
Infrastructure_Enum_Values = ["auto", "generic", "azure", "aws", "gcp", "azure_stack_hci", "azure_stack_hub", "azure_stack_edge", "vsphere"]

Azure_PublicCloudName = 'AZUREPUBLICCLOUD'
Azure_USGovCloudName = 'AZUREUSGOVERNMENTCLOUD'
Azure_DogfoodCloudName = 'AZUREDOGFOOD'
PublicCloud_OriginalName = 'AZURECLOUD'
USGovCloud_OriginalName = 'AZUREUSGOVERNMENT'
Dogfood_RMEndpoint = 'https://api-dogfood.resources.windows-int.net/'
Helm_Environment_File_Fault_Type = 'helm-environment-file-error'
Invalid_Location_Fault_Type = 'location-validation-error'
Load_Kubeconfig_Fault_Type = 'kubeconfig-load-error'
Read_ConfigMap_Fault_Type = 'configmap-read-error'
Get_ResourceProvider_Fault_Type = 'resource-provider-fetch-error'
Get_ConnectedCluster_Fault_Type = 'connected-cluster-fetch-error'
Create_ConnectedCluster_Fault_Type = 'connected-cluster-create-error'
Delete_ConnectedCluster_Fault_Type = 'connected-cluster-delete-error'
Bad_DeleteRequest_Fault_Type = 'bad-delete-request-error'
Cluster_Already_Onboarded_Fault_Type = 'cluster-already-onboarded-error'
Resource_Already_Exists_Fault_Type = 'resource-already-exists-error'
Resource_Does_Not_Exist_Fault_Type = 'resource-does-not-exist-error'
Create_ResourceGroup_Fault_Type = 'resource-group-creation-error'
Add_HelmRepo_Fault_Type = 'helm-repo-add-error'
List_HelmRelease_Fault_Type = 'helm-list-release-error'
KeyPair_Generate_Fault_Type = 'keypair-generation-error'
PublicKey_Export_Fault_Type = 'publickey-export-error'
PrivateKey_Export_Fault_Type = 'privatekey-export-error'
Install_HelmRelease_Fault_Type = 'helm-release-install-error'
Delete_HelmRelease_Fault_Type = 'helm-release-delete-error'
Check_PodStatus_Fault_Type = 'check-pod-status-error'
Kubernetes_Connectivity_FaultType = 'kubernetes-cluster-connection-error'
Helm_Version_Fault_Type = 'helm-not-updated-error'
Check_HelmVersion_Fault_Type = 'helm-version-check-error'
Helm_Installation_Fault_Type = 'helm-not-installed-error'
Check_HelmInstallation_Fault_Type = 'check-helm-installed-error'
Get_HelmRegistery_Path_Fault_Type = 'helm-registry-path-fetch-error'
Pull_HelmChart_Fault_Type = 'helm-chart-pull-error'
Export_HelmChart_Fault_Type = 'helm-chart-export-error'
Get_Kubernetes_Version_Fault_Type = 'kubernetes-get-version-error'
Get_Kubernetes_Distro_Fault_Type = 'kubernetes-get-distribution-error'
Get_Kubernetes_Namespace_Fault_Type = 'kubernetes-get-namespace-error'
Update_Agent_Success = 'Agents for Connected Cluster {} have been updated successfully'
Update_Agent_Failure = 'Error while updating agents. Please run \"kubectl get pods -n azure-arc\" to check the pods in case of timeout error. Error: {}'
Cluster_Info_Not_Found_Type = 'Error while finding current cluster server details'
Kubeconfig_Failed_To_Load_Fault_Type = "failed-to-load-kubeconfig-file"
Proxy_Cert_Path_Does_Not_Exist_Fault_Type = 'proxy-cert-path-does-not-exist-error'
Proxy_Cert_Path_Does_Not_Exist_Error = 'Proxy cert path {} does not exist. Please check the path provided'
Get_Kubernetes_Infra_Fault_Type = 'kubernetes-get-infrastructure-error'
No_Param_Error = 'No parmeters were specified with update command. Please run az connectedk8s update --help to check parameters available for update'
EnableProxy_Conflict_Error = 'Conflict detected: --disable-proxy can not be set with --https-proxy, --http-proxy, --proxy-skip-range and --proxy-cert at the same time. Please run az connectedk8s update --help for more information about the parameters'
Manual_Upgrade_Called_In_Auto_Update_Enabled = 'Manual Upgrade was called while in auto_Update enabled mode'
Upgrade_Agent_Success = 'Agents for Connected Cluster {} have been upgraded successfully'
Upgrade_Agent_Failure = 'Error while upgrading agents. Please run \"kubectl get pods -n azure-arc\" to check the pods in case of timeout error. Error: {}'
