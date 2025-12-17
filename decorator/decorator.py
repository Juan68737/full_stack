import time
'''
def timer_dec(base_fun):
    #Code to decorate
    
    return enhanced_fn

@timer_dec
def brew_tea():
    #Code to brew

brew_tea()
'''

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        result = base_fn(*args, **kwargs) #not the same, we are unpacking
        end_time = time.time()
        print(f"Task Time: {end_time-start_time} seconds")
        return result
    return enhanced_fn

@timer_dec
def brew_tea(tea_type, steep_type):
    print("Brewing Tea! ...")
    time.sleep(1)
    print("Tea is Ready! ...")

@timer_dec
def brew_matcha():
    print("Making matcha! ...")
    time.sleep(1)
    print("Matcha is Ready! ...")

brew_tea("green", 1)
brew_matcha()

 