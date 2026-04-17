from traceback import print_exception


skills = ["python", "AI", "Automation", "Github"]
print(skills)
print(skills[0])
print(skills[2])

tools = ["VS code", "python"]
tools.append("Github")

print(tools)

person = {
	"name": "kev",
	"role": "AI consultant",
	"experience": 2,
}

print(person["name"])
print(person["role"])
print(person["experience"])

profile = {
	"name": "kev",
	"skills": ["python", "AI", "Automation", "Github"],
}
print(profile["skills"])
print(profile["skills"][1])

projects = [
	{
		 "name": "AI prompt Organizer",
		 "status": "in progress",

    },
	{
		"name": "AI content generator",
		"status": "planed"
    }
	
]

print(projects[1]["name"])
print(projects[1]["status"])

project1 = [
	{
		"name": "AI Directory Generator",
		"status": "idea",
    },
	{ 
		"name": "AI Directory keyword",
		"status": "in progress",
	}

]
print(project1[1]["name"])
print(project1[1]["status"])
