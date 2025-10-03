import hashlib
import json
import regex

class User_Auth:
    FILE_NAME_JSON = 'user_data.json'

    def __init__(self):
        self.email = ''
        self.password = ''
        self.user = {}
    
    def store_in_file(self):
        try:
            with open(self.FILE_NAME_JSON, 'r') as file:
                file_content = json.load(file)
        except:
            file_content = []
            print('file does not exist, creating new one...')

        if (not isinstance(file_content, list)):
            return

        if (not len(file_content) > 0):
            with open(self.FILE_NAME_JSON, 'w') as file:
                json.dump([self.user], file, indent=2)
        else:
            file_content.append(self.user)
            with open(self.FILE_NAME_JSON, 'w') as file:
                json.dump(file_content, file, indent=2)
    
    def update_in_file(self):
        with open(self.FILE_NAME_JSON, 'w') as file:
            json.dump(self.user, file, indent=2)

    def read_from_file(self):
        try:
            with open(self.FILE_NAME_JSON, 'r') as file:
                return json.load(file)
        except:
            return []

    def is_valid_email(self, email):
        pat = regex.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')
        return bool(pat.fullmatch(email))

    def register(self):
        self.email = input('Please enter email: ').lower()
        self.password = input('Please enter password: ')

        if self.email:
            if not self.is_valid_email(self.email):
                print('Invalid email entered')
                return

            if self.is_email_existed():
                while self.is_email_existed():
                   self.email = input('Email already exist please enter different: ').lower()

        if self.password:
            self.password = hashlib.sha256(self.password.encode()).hexdigest()

        self.user['email'] = self.email
        self.user['password'] = self.password

        self.store_in_file()
    
    def is_valid_credentials(self, email, password):
        if not email or not password:
            print("Email or password missing")
            return False

        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        user_stored_data = self.read_from_file()
        selected_data = [x for i, x in enumerate(user_stored_data) if x['email'] == email]

        if not len(selected_data):
            return False

        if selected_data[0]['password'] == hashed_pass and selected_data[0]['email'] == email:
            return True

    def login(self):
        email = input('Enter email: ').lower()
        password = input('Enter passord: ')

        if not self.is_valid_email(email):
            print('Invalid email entered') 
            return ''

        if not self.is_valid_credentials(email, password):
            print('Invalid Email or Password, Please try again')
            return ''

        print('Login successfull!!')
        return email      

    def is_email_existed(self):
        user_stored_data = self.read_from_file()
        if (not len(user_stored_data) > 0):
            return False
        selected_data = list(filter(lambda x: x['email'] == self.email, user_stored_data)) or []
        return len(selected_data) > 0

    def logout(self):
        print('Signing out....')

class User_task(User_Auth):
    
    def __init__(self):
        super()
        self.data = self.read_from_file()
        self.task = []
        self.task_count = 0

    def extract_data(self, email):
        data = [[i,x] for i, x in enumerate(self.data) if x['email'] == email]
        user = data[0][1]
        indx = data[0][0]

        return {'index': indx, 'user': user}
    
    def update_file(self, email):
        selected_data = self.extract_data(email)
        self.data[selected_data['index']]['task'] = self.task
        self.user = self.data
        self.update_in_file()

    def add_task(self, email):
        task_description = input('Enter task description: ')
        selected_data = self.extract_data(email)

        self.task.append({'id': self.task_count, 'task': task_description, 'status': 'pending'})
        self.data[selected_data['index']]['task'] = self.task

        self.user = self.data
        self.update_in_file()
        self.task_count += 1  # increment ID for new task

        print('Task added successfully!!')

    def view_task(self, email):
        data = list(filter(lambda x: x['email'] == email, self.user))
        print(f"Here is your task: {data[0]['task']}")

    def delete(self, email):
        try:
            id = int(input('Please enter Id of task you want to delete: '))
            self.task.pop(id)
            self.update_file(email)
        except:
            print('invalid id')

    def completed(self, email):
        try:
            id = int(input('Please enter Id of task completed: '))
            data = [[i,x] for i, x in enumerate(self.task) if x['id'] == id]
            data[0][1]['status'] = 'completed'
            self.task[data[0][0]] = data[0][1]

            self.update_file(email)
        except:
            print('invalid id')

if __name__ == "__main__":
    auth = User_Auth()
    while True:
        chooise = input('What you want to do: register (r) or login (l) or quit (q) ? ').lower()
        match chooise:
            case 'r':
                auth.register()
            case 'l':
                email = auth.login()
                if not len(email):
                    break
                task = User_task()
                while True:
                    task_chooise = input("\n Options: Add Task (add) \n View Task (view) \n Mark As Completed (completed) \n Delete Task (delete) \n logout (logout) \n").lower()
                    match task_chooise:
                        case 'add':
                            task.add_task(email)
                        case 'view':
                            task.view_task(email)
                        case 'completed':
                            task.completed(email)
                        case 'delete':
                            task.delete(email)
                        case 'logout':
                            auth.logout()
                            break
                        case _:
                            print('Unknow command')
                            break
            case 'q':
                break

            case _:
                print('unknown command')
                break
