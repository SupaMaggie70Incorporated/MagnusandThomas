import platform
printableList = [platform.machine(),"\n",platform.processor(),"\n",platform.system(),"\n",platform.node()]
pylog = open("LOG.PYLOG","wt")
pylog.writelines(printableList)
pylog.close()