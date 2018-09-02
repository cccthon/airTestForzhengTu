from airtest.core.api import *
from pymouse import *
from pykeyboard import PyKeyboard
import os

itemDir = 'item/'
shopDir = 'shop/'
npcDir = 'npc/'
menuDir = 'menu/'
caveDir = 'cave/'

m = PyMouse() 
k = PyKeyboard()

print(dir(k))

def move_to_npc(npc='',existPng=''):
    #open near player dialog
    k.tap_key("f")
    #switch near npc
    touch(Template(menuDir + "near_player_npc.png"))
    for i in range(10):
        indexKey = npc.split("f_")[-1][0]
        k.tap_key(indexKey)
        if exists(Template(npc)):
            touch(Template(npc))
            # touch(Template("zhufu.png"),times=2)
            touch(Template("f_move.png"))
            # k.tap_key("f")
            k.tap_key(k.escape_key)
            break
    print("wait npc_zhdhj found.")
    wait(Template(existPng))

#sell list
def sell_list():
    #get sell item
    k.tap_key("b")
    sellItems = []
    for i in os.listdir(itemDir):
        if exists(Template(itemDir + i)):
            sellItems.append(itemDir + i)
    k.tap_key("b")
    # print("sellItems:", sellItems)
    return sellItems
    

#sell items
def sell_items(sellItems=''):
    sleep(1)
    if exists(Template(shopDir + "dp_zhd.png")):
        sleep(0.5)
        touch(Template(shopDir + "dp_zhd_yh.png"), times=2)
    else:
        touch(Template(npcDir + "npc_zhdhj.png"))
        sleep(0.5)
        touch(Template(shopDir + "dp_zhd_yh.png"), times=2)

    for sellItem in sellItems:
        sleep(0.5)
        # swipe(Template(sellItem),Template(shopDir + "dp_zhd_yhp.png",target_pos=9),vector=[-1, 0.4643])
        touch(Template(sellItem))
        sleep(0.2)
        swipe(Template(sellItem),Template(shopDir + "dp_zhd_yhp.png"), vector=[-0.3798, 0.0124])
        sleep(0.2)
        touch(Template(shopDir + "dp_zhd_yhp.png"))



if __name__ == '__main__':
    connect_device("Windows:///?title_re=征途驱魔人模拟器.*")
    #go city
    k.tap_key(k.function_keys[11])
    sleep(1)
    sell_list = sell_list()
    move_to_npc(npc="f_zhdhj.png",existPng=shopDir + "dp_zhd.png")
    sell_items(sell_list)
    move_to_npc(npc="f_chuansongshi.png",existPng=menuDir + "css_jingguaidong.png")

    touch(Template(menuDir + "css_jingguaidong.png"))
    sleep(1)
    touch(Template(caveDir + "jingguaidong.png"))
    sleep(1)
    #进入洞穴后上马
    k.tap_key("t")
    ##k.tap_key(k.function_keys[12])
    k.tap_key("m")
    touch(Template("jg1.png"))
    k.tap_key("m")
    sleep(6)
    #开启自动打怪
    k.press_key(k.control_key)
    k.tap_key("z")
    k.release_key(k.control_key)
