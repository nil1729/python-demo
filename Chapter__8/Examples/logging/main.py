def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info(f'Will run with args: {args}, and kwargs: {kwargs}')

        try:
            result = original_function(*args, **kwargs)
        except Exception as err_msg:
            logging.error(err_msg)
        else:
            return result
    
    return wrapper

@my_logger
def display_info(name, age):
    print(f'{name} is {age} years old')

display_info('Nilanjan', 21)
display_info(age=21, name='John')
display_info()