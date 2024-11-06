from app.app import app
from apscheduler.schedulers.background import BackgroundScheduler
from app.agent.agent import Agent

#Initialization of the app and processes
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(Agent().collect_and_send_system_info, 'interval', minutes=1)
    scheduler.start()
    app.run(debug=False, host='0.0.0.0', port=8080)