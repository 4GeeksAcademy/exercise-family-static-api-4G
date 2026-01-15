"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members= [
            {
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "id": self._generate_id(),
                "lucky_numbers": [7, 13, 22]
            },
            {
                "first_name": "Jane", 
                "last_name": self.last_name,
                "age": 35,
                "id": self._generate_id(),
                "lucky_numbers": [10, 14, 3]
            },
            {
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "id": self._generate_id(),
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        new_member = {
            "id": self._generate_id(),
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member.get("lucky_numbers", [])
        }
        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                return self._members.pop(i)

    def get_member(self, id):
       for member in self._members:
           if member ["id"] == id:
               return member

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
