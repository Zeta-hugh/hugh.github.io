# coding=utf-8
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .functions import slider

global slider_angle, svo_slider_angle, svo_classification, mean_allocations


class SliderPrimaryDiscrete(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['slider1',
                   'slider2',
                   'slider3',
                   'slider4',
                   'slider5',
                   'slider6',
                   ]

    def vars_for_template(self):
        return {'slider_items': [1, 2, 3, 4, 5, 6]}

    def before_next_page(self):

        chosen_values = {
            'item1': self.player.slider1,
            'item2': self.player.slider2,
            'item3': self.player.slider3,
            'item4': self.player.slider4,
            'item5': self.player.slider5,
            'item6': self.player.slider6
        }
        mean_allocations = slider.mean_allocations_discrete(chosen_values)
        svo_slider_angle = round(slider.svo_angle(mean_allocations['self'], mean_allocations['other']),2)
        self.player.slider_angle = svo_slider_angle
        self.player.slider_classification = slider.svo_classification(svo_slider_angle)
        print(chosen_values, mean_allocations, svo_slider_angle)


class Start(WaitPage):
    #group_by_arrival_time = True
    body_text = 'Waiting for the other participant.'

    def is_displayed(self):
        return True
    # def before_next_page(self):
    #     return self.player.before_next_page(), self.subsession.creating_session()
class populationalvar(Page):
    #group_by_arrival_time = True
    form_model = 'player'
    form_fields = ['name','age','gender','education','career','contact','subjectid','otherinfo']
    def is_displayed(self):
        return self.round_number == 1

    # def before_next_page(self):
    #     return self.player.before_next_page(), self.subsession.creating_session()


class SVOresult(Page):
    form_model = 'player'

    def is_displayed(self):
        return True
    def before_next_page(self):
    #     self.subsession.creating_session()
        self.player.before_next_page()
    #     return self.subsession.creating_session()
    # def before_next_page(self):
    #      self.subsession.creating_session()
    def vars_for_template(self):
        return self.player.vars_for_template()#svo_slider_angle 继承第一轮，slider_classification 继承第一轮；fake_svo_angle，shared_point选择第一轮赋值


class Accept(Page):
    form_model = 'player'
    form_fields = ['offer_accept']

    def is_displayed(self):
        return True
    def before_next_page(self):
    #     self.subsession.creating_session()
        self.player.before_next_page()
    #     return self.subsession.creating_session()
    # def before_next_page(self):
    #     self.subsession.creating_session()
    def vars_for_template(self):
        return dict(
            self.player.vars_for_template(),
            individual_share_a = self.participant.vars['fshare']
        )

# class ResultsWaitPage(WaitPage):
#	body_text = 'Waiting for other participants.'


class Results(Page):
    form_model = 'player'

    def is_displayed(self):
        return True
    def before_next_page(self):
    #     self.subsession.creating_session()
        self.player.before_next_page()
    #     return self.subsession.creating_session()
    # def before_next_page(self):
    #     self.subsession.creating_session()
    def vars_for_template(self):
        return dict(
            self.player.vars_for_template(),
            individual_share_a=self.participant.vars['fshare']
        )

class Rfpage(Page):
    form_model = 'player'
    form_fields = ['feeling_rating']

    def is_displayed(self):
        return True
    def before_next_page(self):
    #     self.subsession.creating_session()
        self.player.before_next_page()
    #     return self.subsession.creating_session()

    def vars_for_template(self):
        return dict(
            self.player.vars_for_template(),
            individual_share_a=self.participant.vars['fshare']
        )

class Activity_Break(Page):
    form_model = 'player'

    def is_displayed(self):
        return True

    def before_next_page(self):
       # self.subsession.group_randomly(fixed_id_in_group=True)
        return self.subsession.creating_session()
page_sequence = [Start, populationalvar,SliderPrimaryDiscrete, SVOresult, Accept, Results, Rfpage,
                 Activity_Break]  # Responder_preferences,ResultsWaitPage,WaitForProposer,
