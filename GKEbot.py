import telegram 
import requests 
from telegram.bot import Bot 
bot = telegram.Bot(token='6667716259:AAG1F-S_3JfFB09xyYzkYUUl4xkTg9o0s0k') 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
updater = Updater(token='6667716259:AAG1F-S_3JfFB09xyYzkYUUl4xkTg9o0s0k', use_context=True) #Replace TOKEN with your token string 

dispatcher = updater.dispatcher 

# Function for /hi
def hi(update, context):
        bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hey there! \nThis bot helps with general GKE issues. Please type /start to get started..! \n /owner to get to know about me \nConnect with me on LinkedIn /linkedin \nCheck out my GitHub: /github \nRead my articles on Medium: /medium \nSee my contribution on Stack Overflow : /stackoverflow"
        )
hi_handler = CommandHandler('hi', hi)
dispatcher.add_handler(hi_handler)

def owner(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Narayan Murgod (Cloud DevOps/Support engineer) \nCognizant Technology Solutions Pvt Ltd \nHyderabad, India \n2022/02 to Serving notice period \nHere is my resume /resume"
    )
owner_handler = CommandHandler('owner', owner)
dispatcher.add_handler(owner_handler)

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

def infra_autoscaling(update, context):  
    bot.send_message( 
        chat_id=update.effective_chat.id, 
        text="Learn how GKE cluster autoscaler functions - /CA \nCluster autoscaler with node auto-provisioning - /NAP" 
        )
start_value=CommandHandler('infra_autoscaling', infra_autoscaling) 
dispatcher.add_handler (start_value) 

def CA(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="How GKE cluster autoscaler functions: https://medium.com/@narayanmurgod3388/how-gke-cluster-autoscaler-functions-9cf1fdccc867",
        )
upgrade_handler = CommandHandler('CA', CA)
dispatcher.add_handler(upgrade_handler)

def NAP(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Cluster autoscaler with node auto-provisioning: https://medium.com/@narayanmurgod3388/cluster-autoscaler-with-node-auto-provisioning-c2a42c22ee1d",
        )
upgrade_handler = CommandHandler('NAP', NAP)
dispatcher.add_handler(upgrade_handler)

def workload_autoscaling(update, context):  
    bot.send_message( 
        chat_id=update.effective_chat.id, 
        text="Details on HPA - /hpa \ntarget workload for autoscaling is missing - /wl_miss \nMetric for HPA - /metric_hpa \nOperation of an HPA - /hpa_ops \nHPA Does not trigger Scaling Up/Down When Resource Utilization Threshold Is Exceeded - /hpa_algo " 
        )
start_value=CommandHandler('workload_autoscaling', workload_autoscaling) 
dispatcher.add_handler (start_value) 

def hpa(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Horizontal Pod autoscaling (HPA): https://medium.com/@narayanmurgod3388/horizontal-pod-autoscaling-hpa-6c7c86996edb",
        )
upgrade_handler = CommandHandler('hpa', hpa)
dispatcher.add_handler(upgrade_handler)

def wl_miss(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Checking for the presence of the target workload for autoscaling: https://medium.com/@narayanmurgod3388/checking-for-the-presence-of-the-target-workload-for-autoscaling-ecdbb1c1fd0d",
        )
upgrade_handler = CommandHandler('wl_miss', wl_miss)
dispatcher.add_handler(upgrade_handler)

def metric_hpa(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Identifying the Metric for Horizontal Pod Autoscaler (HPA) Autoscaling: https://medium.com/@narayanmurgod3388/identifying-the-metric-for-horizontal-pod-autoscaler-hpa-autoscaling-c244bfdebeec",
        )
upgrade_handler = CommandHandler('metric_hpa', metric_hpa)
dispatcher.add_handler(upgrade_handler)

def hpa_ops(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Comprehending the Operation of an HPA: https://medium.com/@narayanmurgod3388/comprehending-the-operation-of-an-hpa-194432d5867f",
        )
upgrade_handler = CommandHandler('hpa_ops', hpa_ops)
dispatcher.add_handler(upgrade_handler)

def hpa_algo(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="The HPA Does not Trigger Scaling Up/Down When Resource Utilization Threshold Is Exceeded: https://medium.com/@narayanmurgod3388/the-hpa-doesnt-trigger-scaling-up-down-when-resource-utilization-threshold-is-exceeded-487e931a9dc9",
        )
upgrade_handler = CommandHandler('hpa_algo', hpa_algo)
dispatcher.add_handler(upgrade_handler)

def cluster_monitoring(update, context):  
    bot.send_message( 
        chat_id=update.effective_chat.id, 
        text="cluster metrics missing? - /metrics_miss \nIs the missing metric specific to a particular pod, container, or label? - /pod_metric_miss \nmetric server OOM? - /metric_oom" 
        ) 
start_value1=CommandHandler('cluster_monitoring', cluster_monitoring) 
dispatcher.add_handler (start_value1) 

def metrics_miss(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Missing metrics? https://medium.com/@narayanmurgod3388/missing-metrics-3b282ebc8ef9",
        )
upgrade_handler = CommandHandler('metrics_miss', metrics_miss)
dispatcher.add_handler(upgrade_handler)

def pod_metric_miss(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Is the missing metric specific to a particular pod, container, or label? https://medium.com/@narayanmurgod/is-the-missing-metric-specific-to-a-particular-pod-container-or-label-52ecbf4b253d",
        )
upgrade_handler = CommandHandler('pod_metric_miss', pod_metric_miss)
dispatcher.add_handler(upgrade_handler)

def metric_oom(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Is metrics-server experiencing the Out of Memory (OOM) event? https://medium.com/@narayanmurgod/is-metrics-server-experiencing-the-out-of-memory-oom-event-6dd0d524def0",
        )
upgrade_handler = CommandHandler('metric_oom', metric_oom)
dispatcher.add_handler(upgrade_handler)

def resume(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Please find my resume below:",
        reply_markup=telegram.InlineKeyboardMarkup([[
            telegram.InlineKeyboardButton("My Resume", url="https://drive.google.com/file/d/1b5I5R47zruCZz2m-U1KI_yzNFn3fPlxh/view?usp=sharing")
        ]])
    )

resume_handler = CommandHandler('resume', resume)
dispatcher.add_handler(resume_handler)

def linkedin(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Connect with me on LinkedIn:",
        reply_markup=telegram.InlineKeyboardMarkup([[
            telegram.InlineKeyboardButton("Linkedin", url="https://www.linkedin.com/in/narayan-murgod/")
        ]])
    )

start_value2 = CommandHandler('linkedin', linkedin)
dispatcher.add_handler(start_value2)

def github(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Check out my GitHub:",
        reply_markup=telegram.InlineKeyboardMarkup([[
            telegram.InlineKeyboardButton("GitHub", url="https://github.com/narayanmurgod")
        ]])
    )

start_value3 = CommandHandler('github', github)
dispatcher.add_handler(start_value3)

def medium(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Read my articles on Medium:",
        reply_markup=telegram.InlineKeyboardMarkup([[
            telegram.InlineKeyboardButton("Medium", url="https://medium.com/@narayanmurgod")
        ]])
    )
start_value4 = CommandHandler('medium', medium)
dispatcher.add_handler(start_value4)

def stackoverflow(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="See my Stack Overflow profile:",
        reply_markup=telegram.InlineKeyboardMarkup([[
            telegram.InlineKeyboardButton("Stack Overflow", url="https://stackoverflow.com/users/16425408/narayan-murgod?tab=profile")
        ]])
    )

start_value5 = CommandHandler('stackoverflow', stackoverflow)
dispatcher.add_handler(start_value5)

updater.start_polling()
