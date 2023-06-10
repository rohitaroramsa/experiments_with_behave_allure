from behave import __main__ as behave_runner

'''
This file is alternative for running behave CLI commands from Terminal in order to run BDD test cases
'''

if __name__ == '__main__':
    features_path = 'features'
    additional_parameter = '-f allure_behave.formatter:AllureFormatter -o allure_result --no-capture ' \
                           '--no-capture-stderr --no-logcapture --show-timings '
    cli_parameters = additional_parameter + features_path
    # from cli we cam run command behave features --no-capture --no-capture-stderr --no-logcapture --show-timings
    behave_runner.main(cli_parameters)

