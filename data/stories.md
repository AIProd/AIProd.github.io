## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## crop only query resolved
* greet
  - action_greet_user
  - utter_greet
* affirm
  - utter_how_can_i_help
* crop_disease
  - crop_disease_form
  - form{"name":"crop_disease_form"}   
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
  - action_greet_user
  - utter_greet
* affirm
  - utter_how_can_i_help
* crop_disease
  - crop_disease_form
  - form{"name":"crop_disease_form"}   
  - form{"name":null}
* deny
  - utter_manual_intervention

## user deny on conversation saving
* greet
  - action_greet_user
  - utter_greet
* deny
  - utter_goodbye


## greet
* greet 
    - action_greet_user
  
## demo only 
* demo_only
  - action_contact_number_input
  - utter_demo
* goodbye

## demo only 
* demo_only
  - utter_demo
* goodbye

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
    - crop_disease_form
    - form{"name":"crop_disease_form"}
    - slot{"crop":"grapes"}
* choose{"crop":"grapes"}
    - crop_disease_form
* affirm
    - utter_info_link
    - utter_happy


## New Story

* greet
    - utter_greet
* affirm
    - utter_how_can_i_help
    - slot{"crop":"cotton"}
* crop_disease{"crop":"cotton","disease":"jassids"}
    - slot{"crop":"cotton"}
    - slot{"disease":"jassids"}
    - crop_disease_form
    - form{"name":"crop_disease_form"}
    - slot{"crop":"cotton"}
* affirm
    - utter_info_link
    - utter_more
* affirm
    - utter_how_can_i_help
    - slot{"disease":"leaf spot"}
* crop_disease{"disease":"leaf spot"}
    - slot{"disease":"leaf spot"}
    - crop_disease_form
    - form{"name":"crop_disease_form"}
    - slot{"crop":"cotton"}
* deny
    - utter_manual_intervention
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
* affirm
    - utter_how_can_i_help
* crop_disease{"crop":"cotton","disease":"jassids"}
    - slot{"crop":"cotton"}
    - slot{"disease":"jassids"}
    - crop_disease_form
    - form{"name":"crop_disease_form"}
    - slot{"crop":"cotton"}
* affirm
    - utter_info_link
    - utter_more
* affirm
    - utter_how_can_i_help
    - slot{"disease":"leaf spot"}
* crop_disease{"disease":"leaf spot"}
    - slot{"disease":"leaf spot"}
    - crop_disease_form
    - form{"name":"crop_disease_form"}
    - slot{"crop":"cotton"}
* deny
    - utter_manual_intervention
* goodbye
    - utter_goodbye
