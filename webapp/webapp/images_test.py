import os.path

##Testing that image folder exists
def check_images_exist():
    result = False
   
    if os.path.exists("/static/images/chillibeef.jpeg") and os.path.exists("/static/images/crispywontons.jpeg") and os.path.exists("/static/images/duckandpancakes.jpeg") and os.path.exists("/static/images/kingprawnrolls.jpeg") and os.path.exists("webapp/static/images/kungpochicken.jpeg")and os.path.exists("webapp/static/images/porkbaobuns.jpeg") and os.path.exists("webapp/static/images/specialfriedrice.jpeg" and os.path.exists("webapp/static/images/sweetandsourchicken.jpeg")) :
        result = True
    


    return result



