import os
services_list = ['camera', 'keypad', 'fan', 'live', 'gunicorn']
def restart_service(name):
    #print('sudo systemctl restart ' + name + '.service')
    return os.system('sudo systemctl restart ' + name + '.service')
    
def stop_service(name):
    #print('sudo systemctl stop ' + name + '.service')
    return os.system('sudo systemctl stop ' + name + '.service')
    
def service_active(name):
    service_status = os.system('systemctl is-active --quiet ' + name)
    if service_status == 0:
        return True
    else:
        return False
