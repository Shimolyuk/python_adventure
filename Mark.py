from datetime import datetime

idea = "\nA young computer genius named Mark Zuckerberg has the idea to create a famous website."
come_up_name = "\nWould you like to help Mark come up with a name for his project?"
not_able = "\nUnable to come up with a worthy name for his project, Mark decided to create a really cool animal shelter project and called it MuzzleBook."
help_name_company = "\nWhich name do you like better?"
promising_name = "\nWhich one is more promising? Meta-worse, Failsbook or Instadam?"
meta_project = "\nMark decided to call his project Meta-worse."
is_name_successful = "\nWill he have success?"
meta_worse_decided = '\nMeta-worse was good idea. But Mark is thinking to get new media called "Quitter"!'
failsbook = '\nMark goes for Failsbook!'
more_ideas = "\nShould he try get more ideas?"
insta_dam = "\nMark gets new network name idea - Instadam"
insta_dam_details = "\nSince it is only used by people to show off - the name is not liked by many."
quit_insta_dam = "\nDoes Mark have to close Instadam?"
yes_quit_insta_dam = "\nMark closes Instadam."
what_later = "\nDo you want to know what happened after?"
dont_quit_Instadam = "\nMark stays there forever, but the investors all run to a really cool project called _Nology."
type_clearer = "\nPlease write clearer word."
failsbook_result = "\nMany users didn't join this, but they thanked Mark for being honest with himself and the name."
continue_naming = "\nWant to see what happened to the next network name?"

#function making record of the current date and time into log.txt
def log ():
    with open('log.txt', 'a') as log:
        today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        log.write(f"the record done at {today}\n")
        
# function taking in users input yes or no
def yes_no():
    track_yes_no = False  #variable tracking users input yes or no
    while track_yes_no == False:
        output=input("\nSay yes or no:")
        if (output == 'Yes') or (output == 'yes'):
            return(True)
        elif (output == 'No') or (output == 'no'):
                return(False)

#function that runs the blocks of scenario       
def choose_project_name():
    track_answer = False #variable tracking user's answers
    print(help_name_company) #"Which name do you like better? Meta-worse, Failsbook or Instadam?"
    while track_answer == False:
        decision = input(promising_name) #"Which one is more promising? Meta-worse, Failsbook or Instadam?"
        if (decision == "Meta-worse") or (decision == 'meta-worse'):
            track_answer = True
            print(meta_project) #"Mark decided to call his project Meta-worse."
            print(is_name_successful) #"Will he have success?"
            if yes_no():
                print(meta_worse_decided) # 'Meta-worse was good idea. But Mark changed it for "Quitter"!'
            else:
                print(not_able)#"Unable to come up with a worthy name for his project, Mark decided to create a really cool animal shelter project and called it MuzzleBook."
                log()

        elif (decision == 'Failsbook') or (decision == 'failsbook'):
            track_answer = True
            print(failsbook)#"Mark goes for Failsbook!"
            print(what_later)#Do you want to know what happened after?  
            if yes_no():  
                print(failsbook_result) #"Many users didn't join this, but thanked Mark for being honest with himself and the name."
                print(continue_naming)#"Want to see what happened to the next network name?"
            if yes_no():
                print(meta_project) #"Mark decided to call his project Meta-worse."
                print(is_name_successful) #"Will he have success?"
            if yes_no():
                print(meta_worse_decided) # 'Meta-worse was good idea. But Mark changed it for "Quitter"!'        
            else:
                print(not_able)#"Unable to come up with a worthy name for his project, Mark decided to create a really cool animal shelter project and called it MuzzleBook."
                log()
                
        elif (decision == 'Instadam') or (decision == 'instadam'):
            track_answer = True
            print(insta_dam)#"Mark gets new network name idea - Instadam"
            print(insta_dam_details)#"Since it is only used by people to show off - the name is not liked by many."
            print(quit_insta_dam)#"Does Mark have to close Instadam?"
            if yes_no():
                print(yes_quit_insta_dam)#"Mark closes Instadam."
                print(more_ideas)#"Should he try get more ideas?"
                if yes_no():
                    track_answer = False
                else:
                    print(not_able)#"Unable to come up with a worthy name for his project, Mark decided to create a really cool animal shelter project and called it MuzzleBook."
                    log()
            else:
                print(dont_quit_Instadam)#"Mark stays there forever, but the investors all run to a really cool project called _Nology."
        else:
            print(type_clearer)#"Please write a clearer yes or no."

#function with game scenario loop
def mark_business():
    print(idea)#"A young computer genius named Mark Zuckerberg has the idea to create a famous website."
    print(come_up_name)#"Would you like to help Mark come up with a name for his project?"
    if not yes_no(): #as fas as the function returns false go to not_able
        print(not_able)#"Unable to come up with a worthy name for his project, Mark decided to create a really cool animal shelter project and called it MuzzleBook."
        log()
    else: #otherwise proceed with function choose_project_name
        choose_project_name()
mark_business()
        

    
        
    
