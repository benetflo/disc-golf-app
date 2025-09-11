import json

all_holes_info = []
course_info = {}

def serialize_save_to_file(course_name, course_info):
    with open(f"course_info_{course_name.lower()}.json", "w") as f:
        f.write(json.dumps(course_info))

try:
    course_name = input("Course name: ")
    course_location = input("Course location: ")
    course_length = int(input("Course length: "))
    
    for hole in range(1, course_length + 1):
        
        hole_info = {}

        hole_num = hole
        hole_length = int(input(f"Hole {hole} length in m: "))
        hole_par = int(input(f"Hole {hole} par: "))
        hole_note = input(f"Hole {hole} note: ")

        hole_info["hole_num"] = hole_num
        hole_info["hole_length"] = hole_length
        hole_info["hole_par"] = hole_par
        hole_info["hole_note"] = hole_note

        all_holes_info.append(hole_info)
        
    course_info["course_name"] = course_name
    course_info["location"] = course_location
    course_info["holes"] = all_holes_info
    
    serialize_save_to_file(course_name, course_info)

except Exception as e:
    print(f"Error: {e}")



