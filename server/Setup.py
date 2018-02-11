from cx_Freeze import setup,Executable

target = Executable(
    script="cart.py",
    icon="sc.ico"
    )

setup(name="Smart Shopping Cart",
      version="1.0",
      description="Shopping GUI",
      executables=[target]
      )
