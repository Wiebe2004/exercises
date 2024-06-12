from textwrap import dedent

# Write your code here
def generate_git_script(id):
    string = f'''
    if [ ! -d {id} ]; then
        git clone https://github.com/{id}/project {id}
    else
        (cd {id}; git pull)
    fi
    '''

    return dedent(string).strip()