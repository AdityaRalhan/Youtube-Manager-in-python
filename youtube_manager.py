import json

def load_data():
    try: 
        with open('youtube.txt','r') as file:
            test = json.load(file) 
            # print(test)
            return test # it will go in file, load wtv data is there and also convert it from string into json. THIS IS NOT A LIST
    
    except FileNotFoundError :
        return [] # agar file he nahi mili then return empty list


# this method is a helper method which will help us in saving the info to the file. Basically we can do the working in the other functions and then just call this to save it
def save_data_helper(videos): 
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    print("\n")

    # ENUMERATE so that it adds indexing
    for index, video in enumerate(videos, start=1):
        
        print(f"{index}. {video['name']}, Duration : {video['duration']} ") # video is a dictionary so we need to go in and access the name in it
        
    print("\n")
    print("*" * 70)
         

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name' : name, 'duration' : time}) # storing name and time as objects in the list
    save_data_helper(videos)

def update_video(videos):
    # showing the user a list of all the vids so he can select which to update
    list_all_videos(videos)
    index = int(input("Enter the video number to update : "))
    
    if 1 <= index <= len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter the new video duration : ")
        videos[index - 1] = {'name' : name, 'duration' : time}
        save_data_helper(videos) # calling our function to save our data

    else :
        print('Invalid index selected')

def delete_video(videos):
    # showing him the list we have
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted : "))

    if 1 <= index <= len(videos):
        # del keyword to directly delete it
        del videos[index - 1]
        save_data_helper(videos)

    else :
        print("Invalid video index seleceted")



def main():
    videos = load_data() # will go in file and search for data
    while True:
        print('\n Youtube manager | choose an option')
        print('\n 1. list all youtube videos')
        print('\n 2. add a youtube video')
        print('\n 3. update youtube video details')
        print('\n 4. delete a youtube video')
        print('\n 5. exit the app')

        choice = input (" \n Enter your choice - ")
        # print(videos)

        match choice:
            # notice how it is STRING 1 and not integer because choice is a STRING
            case '1': 
                list_all_videos(videos)

            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break

            case _ :
                print('invalid choice')


if __name__ == "__main__":
    main()