import sqlite3

connection = sqlite3.connect('youtubeVideo.db')
cursor = connection.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
   )
''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("empty video")
    else:
        for row in rows:
            print(row)

def add_video(name, time):
  cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
  connection.commit()

def update_video_details(videoID, new_name, new_time):
  cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, videoID))
  connection.commit()

def delete_video(videoId):
  cursor.execute("DELETE FROM videos WHERE id = ?", (videoId,))
  connection.commit()

def main():

  while True:
    print("\n Youtube manager app with database | choose an option")
    print("1. List all youtube videos")
    print("2. add a youtube video")
    print("3. update a youtube video details")
    print("4. Delete a youtube video")
    print("5. Exit the app")

    choice = input("Please enter your choice: ")

    if choice == '1':
      list_all_videos()

    elif choice == '2':
      name = input("Please enter your video name: ")
      time = input("Please enter your video time: ")
      add_video(name, time) 

    elif choice == '3':
      videoId = int(input("Please enter your video ID to update: "))  
      name = input("Enter the new video name: ") 
      time = input("Enter the new video time: ")
      update_video_details(videoId, name, time)

    elif choice == '4':
      videoId = int(input("Please enter your video ID to delete: "))
      delete_video(videoId)  

    elif choice == '5':
      break

    else:
      print("Invalid choice")  

  connection.close()   

  
if __name__ == '__main__':
  main()