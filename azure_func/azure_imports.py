from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.loganalytics import LogAnalyticsManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.containerservice import ContainerServiceClient
from azure.mgmt.apimanagement import ApiManagementClient
from azure.mgmt.batch import BatchManagementClient
from azure.mgmt.botservice import AzureBotService
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.eventhub import EventHubManagementClient
from azure.mgmt.iothub import IotHubClient
from azure.mgmt.logic import LogicManagementClient
from azure.mgmt.redis import RedisManagementClient
from azure.mgmt.search import SearchManagementClient
from azure.mgmt.servicebus import ServiceBusManagementClient
from azure.mgmt.signalr import SignalRManagementClient
from azure.mgmt.streamanalytics import StreamAnalyticsManagementClient
from azure.mgmt.trafficmanager import TrafficManagerManagementClient
from azure.mgmt.containerservice import ContainerServiceClient
from azure.mgmt.cosmosdb import CosmosDBManagementClient
from azure.mgmt.servicefabric import ServiceFabricManagementClient
from azure.mgmt.cdn import CdnManagementClient
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
from azure.mgmt.devtestlabs import DevTestLabsClient
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.scheduler import SchedulerManagementClient
from azure.mgmt.dns import DnsManagementClient
from azure.mgmt.eventgrid import EventGridManagementClient
from azure.mgmt.recoveryservices import RecoveryServicesClient
from azure.mgmt.recoveryservicesbackup import RecoveryServicesBackupClient
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
from azure.mgmt.resource.locks import ManagementLockClient
from azure.mgmt.storagesync import MicrosoftStorageSync
from azure.mgmt.communication import CommunicationServiceManagementClient
from azure.mgmt.alertsmanagement import AlertsManagementClient
from azure.mgmt.appcontainers import ContainerAppsAPIClient
from azure.mgmt.datamigration import DataMigrationManagementClient