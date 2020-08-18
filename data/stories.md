## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## crop only query resolved
* greet
  - utter_greet
* affirm
  - utter_how_can_i_help
* crop_disease
  - BASF_form                   
  - form{"name":"BASF_form"}   
  - form{"name":null}
* affirm
  - utter_info_link
  - utter_more

## anymore help?  - yes
  - utter_more
* demo_only
  - utter_agent_call

## crop only query not-resolved
* greet
  - utter_greet
* affirm
  - utter_how_can_i_help
* crop_disease
  - BASF_form                   
  - form{"name":"BASF_form"}   
  - form{"name":null}
* deny
  - utter_manual_intervention

## user deny on conversation saving
* greet
  - utter_greet
* deny
  - utter_goodbye

## fallback story
* out_of_scope
  - action_default_fallback

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## say thankyou
  * thankyou
    - utter_thanks

## New Story
* greet
    - utter_greet
* deny
    - utter_goodbye

## New Story
* greet
    - utter_greet
* affirm
    - utter_how_can_i_help
    - slot{"disease":"leaf spot"}
* crop_disease{"disease":"leaf spot"}
    - BASF_form
    - form{"name":"BASF_form"}
    - slot{"crop":"grapes"}
* choose{"crop":"grapes"}
    - BASF_form
* affirm
    - utter_info_link
    - utter_happy

## New Story

* greet
    - utter_greet
* affirm
    - utter_how_can_i_help
* product_only
    - product_input
    - form{"name":"product_input"}
    - form{"disease":"Null"}
* affirm
  - utter_info_link
  - utter_more

## New Story

* greet
    - utter_greet
* affirm
    - utter_how_can_i_help
    - slot{"crop":"cotton"}
* crop_disease{"crop":"cotton","disease":"jassids"}
    - slot{"crop":"cotton"}
    - slot{"disease":"jassids"}
    - BASF_form
    - form{"name":"BASF_form"}
    - slot{"crop":"cotton"}
* affirm
    - utter_info_link
    - utter_more
* affirm
    - utter_how_can_i_help
    - slot{"disease":"leaf spot"}
* crop_disease{"disease":"leaf spot"}
    - slot{"disease":"leaf spot"}
    - BASF_form
    - form{"name":"BASF_form"}
    - slot{"crop":"cotton"}
* deny
    - utter_manual_intervention
* goodbye
    - utter_goodbye
