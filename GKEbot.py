import telegram 
import requests 
from telegram.bot import Bot 
bot = telegram.Bot(token='6667716259:AAG1F-S_3JfFB09xyYzkYUUl4xkTg9o0s0k') 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
updater = Updater(token='6667716259:AAG1F-S_3JfFB09xyYzkYUUl4xkTg9o0s0k', use_context=True) #Replace TOKEN with your token string 

dispatcher = updater.dispatcher 
# function for /start command on telegram 
def start(update, context):  
    bot.send_message( 
        chat_id=update.effective_chat.id, 
        text="Welcome!! \nHope you are having a great time with GKE.\nPlease select the GKE component with which you are experiencing an issue. \nAutopilot cluster related issues - /autopilot \nGKE Infra Autoscaling - /infra_autoscaling \nGKE Workload Autoscaling - /workload_autoscaling \nGKE Cluster Monitoring - /cluster_monitoring \nGKE Control Plane Create,Upgrade,Cluster Operations - /controlplane \nGKE Logging - /gke_logging \nGoogle Managed Prometheus (GMP) - /gmp \nGKE Node Accelerators - /node_gpu \nGKE Node Management - /gke_node GKE \nWorkload Identity - /gke_identity" 
        ) 
start_value0=CommandHandler('start', start) 
dispatcher.add_handler (start_value0) 

# Funtion for /autopilot
def autopilot(update, context):  
    bot.send_message( 
        chat_id=update.effective_chat.id, 
        text="1. Do you have GKE Autopilot upgrade issue then /upgrade \n2. Do you see Cannot create a cluster: 0 nodes registered error - /node_register \n3. Are you facing Node scale up failed: Pod is at risk of not being scheduled error - /pod_fail \n4. Are you experiencing Nodes fail to scale up: Pod zonal resources exceeded - /no_zonal_resource \n5. Autopilot GPU issue? - /gpu_issue \n5. Forbidden & Permission denied errors - /forbideen \n6. Running 3rd party applications on Autopilot - /thirdparty \n7. Workloads are terminating prematurely before completion - /spot_pods" 
        ) 
start_value1=CommandHandler('autopilot', autopilot) 
dispatcher.add_handler (start_value1) 

# Funtion for /upgrade
def upgrade(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Medium article on Autopilot cluster upgrade issue: https://medium.com/@narayanmurgod3388/gke-autopilot-upgrade-issue-53364726f3d6",
        )
upgrade_handler = CommandHandler('upgrade', upgrade)
dispatcher.add_handler(upgrade_handler)

#Funtion for node regsitration
def node_register(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Medium article on Autopilot cluster node registration issue: https://medium.com/@narayanmurgod3388/cannot-create-a-cluster-0-nodes-registered-0d400dba9e36",
        )
upgrade_handler = CommandHandler('node_register', node_register)
dispatcher.add_handler(upgrade_handler)

def pod_fail(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Medium article on Autopilot pod failure: https://medium.com/@narayanmurgod3388/node-scale-up-failed-pod-is-at-risk-of-not-being-scheduled-8d87aed69322",
        )
upgrade_handler = CommandHandler('pod_fail', pod_fail)
dispatcher.add_handler(upgrade_handler)

def no_zonal_resource(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Medium article on Nodes fail to scale up: Pod zonal resources exceeded: https://medium.com/@narayanmurgod3388/nodes-fail-to-scale-up-pod-zonal-resources-exceeded-5b206d35b548",
        )
upgrade_handler = CommandHandler('no_zonal_resource', no_zonal_resource)
dispatcher.add_handler(upgrade_handler)

def gpu_issue(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Medium article on GPU issues on Autopilot: https://medium.com/@narayanmurgod3388/autopilot-gpu-issue-36213dddc93d",
        )
upgrade_handler = CommandHandler('gpu_issue', gpu_issue)
dispatcher.add_handler(upgrade_handler)

def forbideen(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Medium article on Forbidden & Permission denied errors: https://medium.com/@narayanmurgod3388/forbidden-permission-denied-errors-98695e3b5e44",
        )
upgrade_handler = CommandHandler('forbideen', forbideen)
dispatcher.add_handler(upgrade_handler)

def thirdparty(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Medium article on 3rd party applications on Autopilot: https://medium.com/@narayanmurgod3388/3rd-party-applications-on-autopilot-f85e3b8ecde8",
        )
upgrade_handler = CommandHandler('thirdparty', thirdparty)
dispatcher.add_handler(upgrade_handler)

def spot_pods(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Medium article if Workloads are terminating prematurely before completion: https://medium.com/@narayanmurgod3388/workloads-are-terminating-prematurely-before-completion-7321d8bebee6",
        )
upgrade_handler = CommandHandler('spot_pods', spot_pods)
dispatcher.add_handler(upgrade_handler)
updater.start_polling()