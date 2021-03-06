def checkListaOutput(output, input):
    return checkLongitudEsIgual(output, input) and checkCountCanciones(output, input) and checkIntegridad(output, input)


def checkLongitudEsIgual(output, input):
    if len(output) == len(input):
        return True
    else:
        return False


def checkCountCanciones(output, input):
    for cancion in output:
        if output.count(cancion) != input.count(cancion):
            return False
    return True


def checkIntegridad(output, input):
    sortedOutput = sorted(output[:])
    sortedInput = sorted(input[:])
    for index, cancion in enumerate(sortedInput):
        if sortedOutput[index] != sortedInput[index]:
            return False
    return True
