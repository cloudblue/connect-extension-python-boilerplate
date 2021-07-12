# Cookiecutter for CloudBlue Connect Extensions  
  
Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter for CloudBlue Connect Extensions provides a framework for boostraping your custom extensions for Connect.

With this project you can write your own extension to execute either locally or using the Extension as a Service(a.k.a EaaS) module of Connect.

## Features

* Works fit python 3.8 and 3.9
* Bootstraps a custom extension project within seconds
* Provides all needed dependencies
* Provides basic testing functionality including right mockers
* Compatible with github Actions
* Configures project licensing

## Usage

Creating a project that provides a extension package that could be run either using the [Connect CLI](https://github.com/cloudblue/connect-cli) or directly in [Connect](https://connect.cloudblue.com) is simple.

First of all, install in your local machine Cookiecutter, for example you can do it using pip:

	$ pip install cookiecutter

Once cookiecutter is installed you can instantiate it against this repository:

	$ cookiecutter https://github.com/cloudblue/connect-extension-python-boilerplate
 
 You'll be prompted for some values. Provide them and a Connect project will be created for you.

**Warning**: Please change sample data with your own desired information

	project_name [My Awesome Project]: My Awesome Project
	project_slug [my_awesome_project]:
	description [My extension for purchase request processing is super useful!]:
	package_name [connect_ext]: My super awesome package
	package_slug [my_super_awesome_package]:
	author [Globex Corporation]: ISV Inc
	version [0.1.0]: 1.0.0
	Select license:
	1 - Apache Software License 2.0
	2 - MIT
	3 - BSD
	Choose from 1, 2, 3 [1]: 1
	use_github_actions [y]: y
	use_asyncio [y]: n
	Capabilities_Info [In order to initialize your extension, we require to know what capabilities it must support, please answer below y (for Yes) or n (for No). Press enter to continue...]: 
	subscription_process_capabilities_1of6 [Would you like to process asset purchase requests? (default: n)]: y
	subscription_process_capabilities_2of6 [Would you like to process asset change requests? (default: n)]: 
	subscription_process_capabilities_3of6 [Would you like to process asset suspend requests? (default: n)]: 
	subscription_process_capabilities_4of6 [Would you like to process asset resume requests? (default: n)]: 
	subscription_process_capabilities_5of6 [Would you like to process asset cancel requests? (default: n)]: 
	subscription_process_capabilities_6of6 [Would you like to process asset adjustment requests? (default: n)]: 
	subscription_validation_capabilities_1of2 [Would you like to validate asset purchase requests? (default: n)]: y
	subscription_validation_capabilities_2of2 [Would you like to validate asset change requests? (default: n)]: 
	product_capabilities_1of2 [Would you like to execute product actions? (default: n)]: 
	product_capabilities_2of2 [Would you like to process product custom events? (default: n)]: 
	tier_config_process_capabilities_1of2 [Would you like to process tier config setup requests? (default: n)]: 
	tier_config_process_capabilities_2of2 [Would you like to process tier config change requests? (default: n)]: 
	tier_config_validation_capabilities_1of2 [Would you like to validate tier config setup requests? (default: n)]: 
	tier_config_validation_capabilities_2of2 [Would you like to validate tier config change requests? (default: n)]: y
	Done! Your extension project is ready to go!

Now you can access your recently created extension folder and take a look arround it:

	$ cd my_awesome_project
	$ ls

Starting here, if you want you can put your project on a git repository, for example at github:

	$ git init
	$ git add .
	$ git commit -m "first commit"
	$ git remote add origin https://github.com/cloudblue/my_custom_extension.git
	$ git push -u origin master

In the use case that you decided to use github actions, you will notice that a first CI task will run, this one will run the sample test

## Creating your own extension

First, edit the `extension.json` file, this file is a descriptor that can be read by Connect as well as Connect CLI to understand your extension. Please ensure that all properties are defined. On the capabilities dictionary, you can find the capabilities your extension is able to manage and also the states of each one.

The code of your extension must be defined on the `extension.py` file; here is where the system will find your function and execute it, either locally or remotely, depending of your election.

Job done? Try to run it locally!

If you prefer try it from Connect CLI, go ahead and execute the following from your terminal:

	$ ccli project extension bootstrap

	************************************************************

	My Awesome Extension version 1.0.0

	************************************************************

	Welcome to My Awesome Extension !

	My extension for purchase request processing is super useful!

	License

	My Awesome Extension is licensed under the Apache Software License 2.0 license.
