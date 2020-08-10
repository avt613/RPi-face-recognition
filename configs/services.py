import os
def restart_service(name):
    #print('sudo systemctl restart ' + name + '.service')
    return os.system('sudo systemctl restart ' + name + '.service')
    
def stop_service(name):
    #print('sudo systemctl stop ' + name + '.service')
    return os.system('sudo systemctl stop ' + name + '.service')
