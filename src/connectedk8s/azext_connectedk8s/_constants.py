# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


# pylint: disable=line-too-long

Distribution_Enum_Values = ["auto", "generic", "openshift", "rancher_rke", "kind", "k3s", "minikube", "gke", "eks", "aks", "aks_management", "aks_workload", "capz", "aks_engine", "tkg"]
Infrastructure_Enum_Values = ["auto", "generic", "azure", "aws", "gcp", "azure_stack_hci", "azure_stack_hub", "azure_stack_edge", "vsphere", "windows_server"]
Feature_Values = ["cluster-connect", "azure-rbac", "custom-locations"]
Custom_Locations_Provider_Namespace = 'Microsoft.ExtendedLocation'
Connected_Cluster_Provider_Namespace = 'Microsoft.Kubernetes'
Kubernetes_Configuration_Provider_Namespace = 'Microsoft.KubernetesConfiguration'
Arc_Namespace = 'azure-arc'
AZURE_IDENTITY_CERTIFICATE_SECRET = 'azure-identity-certificate'
ISO_861_Time_format = "%Y-%m-%dT%H:%M:%SZ"

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
Get_Credentials_Failed_Fault_Type = 'failed-to-get-list-cluster-user-credentials'
Failed_To_Merge_Credentials_Fault_Type = "failed-to-merge-credentials"
Kubeconfig_Failed_To_Load_Fault_Type = "failed-to-load-kubeconfig-file"
Failed_To_Load_K8s_Configuration_Fault_Type = "failed-to-load-kubernetes-configuration"
Failed_To_Merge_Kubeconfig_File = "failed-to-merge-kubeconfig-file"
Different_Object_With_Same_Name_Fault_Type = "Kubeconfig has an object with same name"
Download_Exe_Fault_Type = "Error while downloading client proxy executable from storage account"
Create_Directory_Fault_Type = "Error while creating directory for placing the executable"
Run_Clientproxy_Fault_Type = "Error while starting client proxy process."
Post_Hybridconn_Fault_Type = "Error while posting hybrid connection details to proxy process"
Post_RefreshToken_Fault_Type = "Error while posting refresh token details to proxy process"
Merge_Kubeconfig_Fault_Type = "Error while merging kubeconfig."
Create_CSPExe_Fault_Type = "Error while creating csp executable"
Remove_Config_Fault_Type = "Error while removing old csp config"
Load_Creds_Fault_Type = "Error while loading accessToken.json"
Creds_NotFound_Fault_Type = "Credentials of user not found"
Create_Config_Fault_Type = "Error while creating config file for proxy"
Run_RefreshThread_Fault_Type = "Error while starting refresh thread"
Load_Kubeconfig_Fault_Type = "Error while loading kubeconfig"
Run_Check_CSP_Thread_Fault_Type = "Error while starting 'check csp thread'."
Proxy_Closed_Externally_Fault_Type = "Proxy closed externally."
Client_Proxy_Port_Fault_Type = "Client proxy port was in use."
Unsupported_Fault_Type = "Error while checking operating system.Unsupported OS detected."
Port_Check_Fault_Type = "Error while checking if port is in use."
Kubeconfig_Failed_To_Load_Fault_Type = "failed-to-load-kubeconfig-file"
Proxy_Cert_Path_Does_Not_Exist_Fault_Type = 'proxy-cert-path-does-not-exist-error'
Proxy_Cert_Path_Does_Not_Exist_Error = 'Proxy cert path {} does not exist. Please check the path provided'
Get_Kubernetes_Infra_Fault_Type = 'kubernetes-get-infrastructure-error'
No_Param_Error = 'No parmeters were specified with update command. Please run az connectedk8s update --help to check parameters available for update'
EnableProxy_Conflict_Error = 'Conflict detected: --disable-proxy can not be set with --https-proxy, --http-proxy, --proxy-skip-range and --proxy-cert at the same time. Please run az connectedk8s update --help for more information about the parameters'
Manual_Upgrade_Called_In_Auto_Update_Enabled = 'Manual Upgrade was called while in auto_Update enabled mode'
Upgrade_Agent_Success = 'Agents for Connected Cluster {} have been upgraded successfully'
Upgrade_Agent_Failure = 'Error while upgrading agents. Please run \"kubectl get pods -n azure-arc\" to check the pods in case of timeout error. Error: {}'
Release_Namespace_Not_Found = 'Error while getting azure-arc releasenamespace'
Get_Helm_Values_Failed = 'Error while doing helm get values azure-arc'
Helm_Existing_User_Supplied_Value_Get_Fault = 'Error while loading the user supplied helm values'
Error_Flattening_User_Supplied_Value_Dict = 'Error while flattening the user supplied helm values dict'
Upgrade_RG_Cluster_Name_Conflict = 'The provided cluster name and rg correspond to different cluster'
Corresponding_CC_Resource_Deleted_Fault = 'CC resource corresponding to this cluster has been deleted by the customer'
Kubernetes_Node_Type_Fetch_Fault = 'Error while trying to find a linux/amd64 node for scheduling pods'
Linux_Amd64_Node_Not_Exists = 'Kubernetes cluster doesnt have amd64/linux node'
Operate_RG_Cluster_Name_Conflict = 'The provided cluster name and rg correspond to different cluster being operated on'
Custom_Locations_Registration_Check_Fault_Type = "Error while checking resource provider registration of custom locations."
Custom_Locations_OID_Fetch_Fault_Type = "Error while fetching oid for custom locations."
Application_Details_Not_Provided_For_Azure_RBAC_Fault = 'Application ID or secret not provided for Azure RBAC'
Successfully_Enabled_Features = 'Successsfully enabled features: {} for the Connected Cluster {}'
Successfully_Disabled_Features = 'Successsfully disabled features: {} for the Connected Cluster {}'
Error_enabling_Features = 'Error while updating agents for enabling features. Please run \"kubectl get pods -n azure-arc\" to check the pods in case of timeout error. Error: {}'
Error_disabling_Features = 'Error while updating agents for disabling features. Please run \"kubectl get pods -n azure-arc\" to check the pods in case of timeout error. Error: {}'
Proxy_Kubeconfig_During_Deletion_Fault_Type = 'Encountered proxy kubeconfig during deletion.'
Cant_Create_ClusterRoleBindings_Fault_Type = 'Cannot create cluster role bindings on this Kubernets cluster'
CC_Provider_Namespace_Not_Registered_Fault_Type = "Connected Cluster Provider MS.K8 namespace not registered"

CLIENT_PROXY_VERSION = '1.1.0'
API_SERVER_PORT = 47011
CLIENT_PROXY_PORT = 47010
CLIENTPROXY_CLIENT_ID = '04b07795-8ddb-461a-bbee-02f9e1bf7b46'
API_CALL_RETRIES = 200
DEFAULT_REQUEST_TIMEOUT = 10  # seconds
RELEASE_DATE_WINDOWS = 'release12-03-21'
RELEASE_DATE_LINUX = 'release12-03-21'
CSP_REFRESH_TIME = 300
# refer https://docs.microsoft.com/en-us/rest/api/storageservices/
# naming-and-referencing-containers--blobs--and-metadata#container-names
STORAGE_CONTAINER_NAME_MAX_LENGTH = 63
# URL constants
CSP_Storage_Url = "https://k8sconnectcsp.blob.core.windows.net"
