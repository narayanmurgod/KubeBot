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
        text="Welcome!! \nHope you are having a great day with GKE, Please select the GKE component with which you are experiencing an issue. Autopilot cluster related issues - /autopilot GKE Infra Autoscaling - /infra_autoscaling GKE Workload Autoscaling - /workload_autoscaling GKE Cluster Monitoring - /cluster_monitoring GKE Control Plane Create,Upgrade,Cluster Operations - /controlplane GKE Logging - /gke_logging Google Managed Prometheus (GMP) - /gmp GKE Node Accelerators - /node_gpu GKE Node Management - /gke_node GKE Workload Identity - /gke_identity" 
        ) 
start_value2=CommandHandler('start', start) 
dispatcher.add_handler (start_value2) 
updater.start_polling()