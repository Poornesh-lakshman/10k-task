def check_payment(func):
    def wrapper(status):
        if status == "completed":
            print("Payment completed successfully.")
        elif status == "pending":
            print("Payment is pending.")
        elif status == "failed":
            print("Payment failed.")
        else:
            print("Invalid payment status.")

        return func(status)

    return wrapper


@check_payment
def payment(status):
    print("Payment status checked.")


payment("completed")
payment("pending")
payment("failed")