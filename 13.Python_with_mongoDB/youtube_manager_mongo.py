import os
import pymongo
from dotenv import load_dotenv
from bson import ObjectId
from bson.errors import InvalidId

# -------------------- CONFIG --------------------

load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL")
if not MONGODB_URL:
    raise ValueError("❌ MONGODB_URL not found in .env file")

client = pymongo.MongoClient(MONGODB_URL, tlsAllowInvalidCertificates=True)
db = client["python_ytmanager"]
videos = db["videos"]

print("✅ Database connected successfully")
# -------------------- CRUD FUNCTIONS --------------------

def list_videos():
    print("\n📺 All Videos")
    print("-" * 40)

    for video in videos.find():
        print(f"ID   : {video['_id']}")
        print(f"Name : {video['name']}")
        print(f"Time : {video['time']}")
        print("-" * 40)


def add_video(name: str, time: str):
    videos.insert_one({"name": name, "time": time})
    print("✅ Video added successfully")


def update_video(video_id: str, name: str = "", time: str = ""):
    try:
        update_fields = {}

        if name.strip():
            update_fields["name"] = name
        if time.strip():
            update_fields["time"] = time

        if not update_fields:
            print("⚠️ Nothing to update")
            return

        result = videos.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": update_fields}
        )

        if result.matched_count:
            print("✅ Video updated successfully")
        else:
            print("❌ Video not found")

    except InvalidId:
        print("❌ Invalid video ID")


def delete_video(video_id: str):
    try:
        result = videos.delete_one({"_id": ObjectId(video_id)})

        if result.deleted_count:
            print("🗑️ Video deleted successfully")
        else:
            print("❌ Video not found")

    except InvalidId:
        print("❌ Invalid video ID")

# -------------------- CLI MENU --------------------

def main():
    while True:
        print("""
🎬 YouTube Manager
1. List videos
2. Add video
3. Update video
4. Delete video
5. Exit
""")

        choice = input("👉 Choose option: ").strip()

        match choice:
            case "1":
                list_videos()

            case "2":
                add_video(
                    input("Video name: "),
                    input("Video time: ")
                )

            case "3":
                print("👉 Leave blank to skip a field")
                update_video(
                    input("Video ID: "),
                    input("New name: "),
                    input("New time: ")
                )

            case "4":
                delete_video(input("Video ID: "))

            case "5":
                print("👋 Bye!")
                break

            case _:
                print("❌ Invalid choice")


if __name__ == "__main__":
    main()