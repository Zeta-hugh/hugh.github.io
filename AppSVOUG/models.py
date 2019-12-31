from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from .functions import slider
import random


author = 'Hao Yu'

doc = """
This is used for experiment combined with both svo and ug paradigm.
"""


class Constants(BaseConstants):
    name_in_url = 'AppSVOUG'
    players_per_group = None
    num_rounds = 50
    endowment = 100
    instructions_slider = 'AppSVOUG/SliderInstructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        import random,sys
        fangle =[]
        fshare =[]
        if self.round_number >= 1:
            for i in range(50):
                fangle.append(round(random.uniform(-16.26, 61.39), 2))
                fshare.append(round(random.uniform(1, 100)))
            for player in self.get_players():
                part_id= player.participant.id
                round_numbers = list(range(0,Constants.num_rounds))
                rsn = random.choice(round_numbers)
                player.participant.vars['fangle'] = fangle[rsn],
                player.participant.vars['fshare'] = fshare[rsn]
            print(player.participant.vars['fangle'],player.participant.vars['fshare'])
        return(player.participant.vars['fangle'],player.participant.vars['fshare'])

    # def before_next_page(self):
    #     self.fake_svo_angle = self.participant.vars['fangle'][0]
    #     self.fake_svo_classification = slider.svo_classification(self.fake_svo_angle)
    #     self.individual_share_a = c(self.participant.vars['fshare'])
    #     self.shared_point = c(Constants.endowment - self.participant.vars['fshare'])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def before_next_page(self):
        self.fake_svo_angle = self.participant.vars['fangle'][0]
        self.fake_svo_classification = slider.svo_classification(self.fake_svo_angle)
        self.individual_share_a = self.participant.vars['fshare']
        self.shared_point = Constants.endowment - self.participant.vars['fshare']

    def set_payoff(self):
        """Calculate payoff, to be implemented later """
        self.payoff = 0

    slider1 = models.FloatField()
    slider2 = models.FloatField()
    slider3 = models.FloatField()
    slider4 = models.FloatField()
    slider5 = models.FloatField()
    slider6 = models.FloatField()
    offer_accept = models.BooleanField(choices=[[True, u'接受'], [False, u'不接受']],
                                       widget=widgets.RadioSelectHorizontal, label=u'你是否接受这个方案?')
    slider_angle = models.DecimalField(decimal_places=2, max_digits=5)
    slider_classification = models.CharField()
    fake_svo_angle = models.DecimalField(decimal_places=2, max_digits=5)
    fake_svo_classification = models.CharField()
    individual_share_a = models.IntegerField()
    shared_point = models.IntegerField()
    feeling_rating = models.IntegerField()
    name = models.StringField(label = u'请输入您的姓名')
    age = models.IntegerField(label=u'请输入您的年龄')
    gender = models.IntegerField(label=u'请输入您的性别',choices=[[1,u'男'],[2,u'女']])
    education = models.StringField(label=u'请输入您的受教育程度',blank=True,choices=[u'小学',u'中学',u'高中',u'大学',]
                                   + [u'大学后进阶教育 %d 年' %y for y in range(1,10)] +[u'持续进阶教育达到 10年及以上',])
    career = models.StringField(label = u'请输入您的职业')
    contact = models.StringField(label = u'请输入您的联系方式（支付宝绑定的手机号）')
    subjectid = models.StringField(label=u'请输入您的身份证号（用于报销凭证）')
    otherinfo = models.StringField(label = u'如有被试费用相关信息请在此处，请在此处说明')
    def vars_for_template(self):
        if self.round_number ==1:
            print (self.participant.vars['fangle'][0], self.participant.vars['fshare'])
            return {'svo_slider_angle': self.slider_angle,
                    'slider_classification': slider.svo_classification(self.slider_angle),
                    'fake_svo_angle': self.participant.vars['fangle'][0],
                    'fake_svo_classification': slider.svo_classification(self.fake_svo_angle),
                    'individual_share_a':self.participant.vars['fshare'],
                    'shared_point': Constants.endowment - self.participant.vars['fshare'],
                    }
        else:
            round_1_player = self.in_round(1)
            return {'svo_slider_angle': round_1_player.slider_angle,
                    'slider_classification': round_1_player.slider_classification,
                    'fake_svo_angle': self.participant.vars['fangle'][0],
                    'fake_svo_classification': slider.svo_classification(self.fake_svo_angle),
                    'individual_share_a':self.participant.vars['fshare'],
                    'shared_point': Constants.endowment - self.participant.vars['fshare']
                    }