#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow


ha_dict = {
    u'吼啊': [u'好啊', u'吼啊', u'吼蛙'],
    u'当然啦': [u'裆燃啦'],
    u'见着风，是得雨' : [],
    u'钦定': [u'硬点'],
    u'无可奉告': [],
    u'你问我支持不支持': [u'滋磁不滋磁'],
    u'你们还要学习一个': [u'鞋洗一个'],
    u'非常熟悉西方的这一套的value': [u'非常熟悉西方的这一套理论'],
    u'我是身经百战，见得多了': [u'见的多了'],
    u'西方的哪一个国家我没去过': [],
    u'美国的华莱士比你们不知道高到哪里去了，我跟他谈笑风生': [u'XX比你不知道高到哪里去了'],
    u'媒体还是要提高自己的知识水平': [u'提高姿势水平'],
    u'识得唔识得啊': [],
    u'我也为你们着急啊，真的': [u'我为你们拙计', u'捉急'],
    u'你们有一个好，全世界跑到什么地方，你们比其他的西方记者跑得还快': [u'跑得比香港记者快'],
    u'too young, too simple, sometimes naïve': [u'图样图森破', u'拿衣服'],
    u'图样': [u'图样图森破', u'拿衣服'],
    u'我今天是作为一个长者来跟你们讲的': [u'长者'],
    u'我有必要告诉你们一点人生的经验': [],
    u'坠吼的': [u'中国有一句话叫闷声大发财，这是最好的', u'闷声发大财', u'这是坠吼的'],
    u'见到你们这样热情啊，一句话不说也不好': [],
    u'如果将来宣传报道有偏差，你们要负责': [u'你们也是要负责的'],
    u'连任也要按照香港的法律啊，当然我们的决定权也是很重要的': [u'都要按照基本法'],
    u'你们啊，不要想喜欢弄个大新闻，说现在已经钦定了，再把我批判一番': [u'搞个大新闻'],
    u'I am angry!': [u'爱慕安格瑞', u'按M安轨'],
    u'你们这样子啊，是不行的！': [],
    u'今天是得罪了你们一下！': [],
    u'time flies very fast': [],
    u'all men are created equal': [],
    u'very frankly speaking': [],
    u'you mean I\'m a dictatorship?': [],
    u'big mistake!': [],
    u'即使在非常时期，政府还是能很理智和克制': [],
    u'同学们，大家起来!': [],
    u'西方的哪一部电影我没看过': [],
    u'军队一律不得经商': [],
    u'engineering drawing': [],
    u'鸭嘴笔': [],
    u'这个效率，efficiency': [],
    u'apply for professor': [],
    u'这个报告经过好几百个教授一致通过': [],
    u'人呐都不知道自己不可以预料': [u'一个人的命运当然要靠自我奋斗', u'但是也要考虑历史的行程'],
    u'一个人的命运当然要靠自我奋斗, 但是也要考虑历史的行程': [u'一个人的命运当然要靠自我奋斗', u'但是也要考虑历史的行程', u'人呐都不知道自己不可以预料'],
    u'我说另请高明吧！我实在也不是谦虚，我一个上海市委书记怎么到北京来了呢？': [u'我实在也不是谦虚', u'中央已经决定啦，由你来当总书记'],
    u'后来我就念了两句诗，叫“苟利国家生死以，岂因祸福避趋之”': [u'苟', u'苟利国家生死以，岂因祸福避趋之'],
    u'很惭愧，就做了一点微小的工作，谢谢大家': [],
    u'你们给我搞的这本东西，excited！': [u'亦可赛艇', u'一颗赛艇', u'exciting'],
    u'一颗赛艇， 亦可赛艇': [u'你们给我搞的这本东西，excited！', u'水能载舟亦可赛艇', u'exciting'],
    }


def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`. Not so useful, as
    # the `wf` object created in `if __name__ ...` below is global.
    #
    # Your imports go here if you want to catch import errors (not a bad idea)
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    #import somemodule
    #import anothermodule
    # Get args from Workflow, already in normalized Unicode
    args = wf.args

    a = []
    for arg in args:
        for key in ha_dict.keys():
            if (arg in key):
                wf.add_item(title=key, valid=True, arg=key, copytext=key)
                a.append(key)
                if (ha_dict[key]):
                    for item in ha_dict[key]:
                        wf.add_item(title=item, valid=True, arg=item, copytext=item)
                        a.append(item)
    # Do stuff here ...

    # Add an item to Alfred feedback
    # wf.add_item(u'Item title', u'Item subtitle')

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but Alfred won't be listening
    # any more...
    if (a):
        wf.send_feedback()
    else:
        wf.add_item(u'无可奉告', valid=True, arg=u'无可奉告', copytext=u'无可奉告')
        wf.send_feedback()
    return 0


if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))
