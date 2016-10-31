# How to add your task

## git

First of all, make sure you work in a separate branch:

```bash
$ git pull origin master            # get latest version of the master branch
$ git checkout -b web/phpiserable   # category/problem name
Switched to a new branch 'web/phpiserable'
```

Make your changes, commit and push to your branch, then merge:

```
$ git add grader.py
$ git commit -m "Grader example"
$ git push origin web/phpiserable 
$ git checkout master
$ git pull origin master   # get latest version of the master branch
$ git merge phpiserable
```



## Task types

There are two types of problems:

- *basic* problems - have only one version.
- *auto-generated* problems - allow for different users to receive different versions of the same problem.




## Basic

Every basic problem needs two components: 

```
├── grader/
    │   └── grader.py
    ├── problem.json
    └── static/
```

A `problem.json` file should look like this:

```json
{"name": "Problem Name",
"score": 10,
"category": "Category Name",
"grader": "misc/myproblem/grader.py",
"description": "Problem text. HTML can be used here.",
"threshold": 0,
"weightmap": {},
"hint": "Hint text. HTML can be used here"}
```

A grading script, written in **Python 3**, should look like this:

```python
def grade(arg, key):
    # note: you can use hashes, generators, and a lot of other stuff.
    # for examples see folder: example_problems
    if "this_is_the_flag" in key:
        return True, "Correct"
    else:
        return False, "Incorrect"
```

Problem loading script is `api_manager.py problems load`.

Suppose you want to create a new problem *PHPiserable*. First, we make a directory for our problem, such as `platform/problems/web/phpiserable/`. Now we place our `problem.json` file and `grader.py` file as following:

```
problems/
└── web/
    └── phpiserable/
        ├── grader/
            │   └── grader.py
            ├── problem.json
            └── static/
```

Check that our `grader` path in `problem.json` points to the grader. **Note** that this path is NOT an absolute path. For `problems/web/phpiserable/grader/grader.py` use following path: `web/phpiserable/grader.py`.

The "threshold" and "weightmap" fields are used to manage problem unlocking. If you would like a problem to always be available, set "threshold" to 0 and "weightmap" to `{}`. Suppose we have four problems "A", "B", "C", and "D". If we want to make "D" unlock if any 2 of "A", "B", or "C" are solved, we set the "weightmap" to `{"A": 1, "B": 1, "C": 1}`, since all these problems are weighted equally, and "threshold" to 2, since we want to unlock the problem when any two problems are solved.

Some problems need to provide additional files for the user to view or download (binaries, encrypted messages, images, etc.). To add static files to your problem, add a `static` folder in the directory for that problem (`/problems/web/phpiserable/static/`, for example) and place any files in that directory that you want to serve statically. Then, in your problem description (or hint), you can link to this file using the URL `/problem-static/[path to problem in problems directory]/[file name]`. Look at the example problem `Sdrawkcab` to see this in action.



## Autogen problems

Automatically generated (autogen) problems allow different teams to receive different versions of the same challenge. For example, the picoCTF 2014 problem `Substitution` (a substitution cipher problem) uses different letter mappings and Disney song lyrics for different problem instances. This has numerous advantages, including the prevention and detection of flag sharing between teams.

Before deploying a competition, you need to generate some number of autogen problem instances per autogen problem. These instances will serve as a pool of possible versions of the problem. During the competition, teams will randomly be assigned one autogen instance from the pool of available instances.

Whereas basic problems have just a `grader` script, autogen problems have both a `grader` and a `generator` script. The `generator` contains code for producing all of the content needed for a given problem instance. The `grader`, as with basic problems, is used to determine whether an flag submitted by a user for a given problem instance is correct.

The `Hidden Message` problem under `example_problems` contains example code for creating an autogen problem. We will use this as a working example of how to develop an autogen problem.

`Generators` implement the following function signature: `generate(random, pid, autogen_tools, n)`, where each argument is as follows:

- *random*: A Python [`random`](https://docs.python.org/3.4/library/random.html) instance, which should be the only source of randomness used to generate the problem. This allows autogen problems to be random, but deterministic, such that regenerating a set of problems will always create identical instances.
- *pid*: The problem id for the autogen problem
- *autogen_tools*: An object supporting the autogen-related functions defined in `api/api/autogen_tools.py`
- *n*: The instance number for the current problem instance being generated

The `generate` function should return a dictionary with three fields: `resource_files` (per-instance files that can be seen by players solving the problem), `static files` (per-instance files hidden from players), and `problem_updates` (what fields in the original `problem.json` object need to be altered for this particular problem instance). 

Take a look at`example_problems/web/hidden-message/grader/generator.py` for an example simple generator that produces a custom problem description for each problem instance.

`Graders` must implement the following function signature: `grade(autogen, key)`, where each argument is as follows:

- *autogen*: An instance of the `GraderProblemInstance` class defined in `api/api/autogen.py`. Notably it has the field`instance` which gives you the instance number (same as `n` in the generator).
- *key*: The flag submitted by the user to be checked for correctness

Graders return a boolean, string pair as with basic problems.

It is very likely that both the problem *generator* and *grader* need to know the value of the flag for the given problem instance. There are two possible methods to share a common flag between the two scripts:

1. Generate the flag in the *generator*, then save it in a static file that is read in by the *grader*.
2. Make the flag deterministic based on the problem instance.

The example problem `Hidden Message` uses the latter strategy. In the generator, it calculates the flag with the following code:

```python
key = "my_key_here"
flag = "flag_" + sha1((str(n) + key).encode('utf-8')).hexdigest()
```

The grader then performs a similar calculation:

```python
secretkey = "my_key_here"
n = autogen.instance
flag = sha1((str(n) + secretkey).encode('utf-8')).hexdigest()
```

Note that autogen problems must set two additional fields in the `problem.json` file. In addition to "grader", there needs to be a "generator" field pointing to the generator script. Also, the "autogen" field must be set to `true`. See`example_problems/web/hidden-message/problem.json` for an example.



## Problem Categories

The category of a problem is specified in the "category" field of the `problem.json` file. Note that there is not a fixed set of categories; you may use any free-form category name. Many features, such as the code to generate problem statistics, will group problems by category name. Thus, it is useful to make sure that you are consistent in your spelling and formatting for each category name.

If you plan on using the existing achievements from picoCTF, you will need to edit the "Category Completion" and "Category Solved 5" achievements based on your new category names.



## Loading Problems

Problems are loaded into the database and set up for deployment using the `api_manager.py` script. To load your problems, run the following command in `~/api`:

`python3 api_manager.py problems load [your problems directory] graders/ ../problem_static`

Note that this will create the `graders` and `problem_static` folder if they do not exists. At present you cannot trivially move the locations of the `graders` and `problem_static` directory since they are explicitly referenced elsewhere.

As always, you must run `devploy` to see your new problems appear.

In addition to loading problems, you must also generate instances for any autogen problems (see previous section) that you may have. To generate 100 problem instances for each autogen problem, you would run the following command:

`python3 api_manager.py autogen build 100`

Note that this command is idempotent. Assuming your autogen instances use only the provided source of randomness, repeatedly running this command will regenerate the exact same set of 100 problem instances.



## Updating and Deleting Problems

In order to update problems, you must first remove the old version of the problems from the database. Currently, this is done by connecting to the database and deleting the problems as follows:

1. Run `mongo pico` (**Note:** since mongo is in docker container, only Bogdan has an access to this `fixthis`)
2. Enter `db.problems.remove()` in the MongoDB terminal
3. Enter `db.submissions.remove()` in the MongoDB terminal (deletes all problem submissions)

Once you have removed the problems, you can load in the new versions as described in the previous section. If any autogen problems have been deleted, you will also need to rebuild the autogen instances.

**Note on updating problems during the live competition**: During the competition, you may want to update problems without clearing out all submissions (step three above). Existing submissions will be correctly associated with an updated problem if both the new and old problem share *exactly the same name*. Thus, if you want to update a problem, but not its name, you need not delete existing submissions. If you change the problem name, you **must** delete existing submissions, or users will receive errors on the "Problems" page. Note that if you change a problem's *grader* and keep existing submissions they will not be reevaluated using the new grader. In other words, if you keep existing submissions to a problem, all correct submissions will always remain correct for the new version of the problem.