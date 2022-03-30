try:
    main()
except LowFuelError as e:
    print(e)
except NotEnoughFuel as e:
    print(e)
except CargoOverload as e:
    print(e)

