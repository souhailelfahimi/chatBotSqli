## Generated Story 3320800183399695936
* get_weater
    - action_ask_GPE
* inform_GPE{"GPE": "italy"}
    - slot{"GPE": "italy"}
    - action_weather

    
## Generated Story -3351152636827275381
* get_weater{"GPE": "London"}
    - slot{"GPE": "London"}
    - action_weather


      
## story_007   
* getCard
    - action_ask_GPE
* inform_GPE{"GPE": "United states"}
    - slot{"GPE": "United_states"}
    - action_ask_type
* inform_type_card{"type_card":"visa"}    
    - slot{"type_card":"visa"}
    - action_card
  
    
## story_010    
* getCard{"GPE":"United states","type_card":"visa"}
    - slot{"GPE": "United stat"}
    - slot{"type_card":"visa"}
    - action_card


            
## Generated Story 4922780951734593234
* getCard{"GPE": "United states"}
    - slot{"GPE": "United states"}
    - action_ask_type
* inform_type_card{"type_card":"visa"}
    - slot{"type_card":"visa"}
    - action_card

        
## Generated Story 4922780951734593235
* getCard{"type_card":"visa"}
    - slot{"type_card":"visa"}
    - action_ask_GPE
* inform_GPE{"GPE":"United states"}
    - slot{"GPE": "United states"}
    - action_card


## story_013        
* goodbye
    - utter_goodbye    
## story_014 
 * greet
    - utter_greet    


## story happy healt check

* healt_check
  - utter_ask_for_service
* inform_app_detection{"service_name":"NCS-PAY"}
  - slot{"service_name":"NCS-PAY"}
  - utter_ask_for_env
* inform_environment_detection{"env_name":"DEV1"}
  - slot{"env_name":"NCS-PAY"}
  - action_healt_check
  
## story happy healt check all given

* healt_check{"service_name":"NCS-PAY","env_name":"DEV1"}
  - slot{"service_name":"NCS-PAY"}
  - slot{"env_name":"NCS-PAY"}
  - action_healt_check  
  
  
## story happy healt check service name is given

* healt_check{"service_name":"NCS-PAY"}
  - slot{"service_name":"NCS-PAY"}
  - utter_ask_for_env
* inform_environment_detection{"env_name":"DEV1"}
  - slot{"env_name":"NCS-PAY"}
  - action_healt_check
  
## story happy healt check service name is given

* healt_check{"env_name":"DEV1"}
  - slot{"env_name":"DEV1"}
  - utter_ask_for_service
* inform_environment_detection{"service_name":"NCS-PAY"}
  - slot{"service_name":"NCS-PAY"}
  - action_healt_check  
## story stackoverflow
* stackoverflow
  - search_stackoverflow  

    