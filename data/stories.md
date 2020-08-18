## search restaurant happy path
* greet
 - utter_how_can_i_help
* search_provider
 - action_facility_search
* thanks
 - utter_noworries
 
## search restaurant + location
* greet
 - utter_how_can_i_help
* search_provider
 - utter_ask_location
* inform
 - action_facility_search
* thanks
 - utter_noworries

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
 