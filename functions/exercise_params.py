def create_profile(name, age, **personal_details):
    profile = {
        'Name': name,
        'Age': age
    }

    profile.update(personal_details)
    return profile

profile = create_profile('Vali Basha', 21, location='RJY', occupation='Data Engineer', hobbies=['reading','travelling'])
print(profile)