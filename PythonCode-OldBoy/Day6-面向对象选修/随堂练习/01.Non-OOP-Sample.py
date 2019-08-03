# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# role 1
name = 'Alex'
role = 'terrorist'
weapon = 'AK47'
life_value = 100

# role 2
name2 = 'Jack'
role2 = 'police'
weapon2 = 'B22'
life_value2 = 100

# role 3
name3 = 'Rain'
role3 = 'terrorist'
weapon3 = 'C33'
life_value3 = 100
money3 = 10000

# role 4
name4 = 'Eric'
role4 = 'police'
weapon4 = 'B51'
life_value4 = 100
money4 = 10000

# 4个角色虽然创建好了，但是有个问题就是，每创建一个角色，我都要单独命名，name1,name2,name3,name4…，后面的调用的时候这个变量名你还都得
# 记着，要是再让多加几个角色，估计调用时就很容易弄混啦，所以我们想一想，能否所有的角色的变量名都是一样的，但调用的时候又能区分开分别是谁？

roles = {
    1:{
        'name':'alex',
        'role':'terrorist',
        'weapon':'AD47',
        'life_value':100,
        'money':15000,
    },
    2:{
        'name':'Jack',
        'role':'police',
        'weapon':'B22',
        'life_value': 100,
        'money': 15000,
    },
    3: {
        'name': 'Rain',
        'role': 'terrorist',
        'weapon': 'C33',
        'life_value': 100,
        'money': 15000,
        },
    4: {
        'name': 'Eirc',
        'role': 'police',
        'weapon': 'B51',
        'life_value': 100,
        'money': 15000,
        },
}

print(roles[1]) #Alex
print(roles[2]) #Jack

# 我们可以把每个功能写成一个函数

'''
def shot(by_who):
    # 开了枪后要减子弹数
    pass
def got_shot(who):
    #中枪后要减血
    who[‘life_value’] -= 10
    pass
def buy_gun(who,gun_name):
    #检查钱够不够,买了枪后要扣钱
    pass

从上面的代码设计中，我看到以下几点缺陷：
1. 每个角色定义的属性名称是一样的，但这种命名规则是我们自己约定的，从程序上来讲，并没有进行属性合法性检测，也就是说role 1定义的代表武器
的属性是weapon, role 2 ,3,4也是一样的，不过如果我在新增一个角色时不小心把weapon 写成了wepon , 这个程序本身是检测 不到的
2. terrorist 和police这2个角色有些功能是不同的，比如police是不能杀人质的，但是terrorist可能，随着这个游戏开发的更复杂，我们
会发现这2个角色后续有更多的不同之处， 但现在的这种写法，我们是没办法 把这2个角色适用的功能区分开来的，也就是说，每个角色都可以直接
调用任意功能，没有任何限制。
3. 我们在上面定义了got_shot()后要减血，也就是说减血这个动作是应该通过被击中这个事件来引起的,我们调用get_shot()，got_shot（）这个函数
再调用每个角色里的life_value变量来减血。 但其实我不通过got_shot()，直接调用角色roles[role_id][‘life_value’] 减血也可以呀，但是
如果这样调用的话，那可以就是简单粗暴啦，因为减血之前其它还应该判断此角色是否穿了防弹衣等，如果穿了的话，伤害值肯定要减少，got_shot()函数
里就做了这样的检测，你这里直接绕过的话，程序就乱了。 因此这里应该设计 成除了通过got_shot(),其它的方式是没有办法给角色减血的，不过在上面
的程序设计里，是没有办法实现的。 
4. 现在需要给所有角色添加一个可以穿防弹衣的功能，那很显然你得在每个角色里放一个属性来存储此角色是否穿 了防弹衣，那就要更改每个角色的代码
，给添加一个新属性，这样太low了，不符合代码可复用的原则

'''

