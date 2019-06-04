> @author BXYMartin@buaa.edu.cn

> @2019-06-04

# UML Testing Service (UTS) v4.1.3
## Prerequisites
### - Linux/MacOS Bash Environment
### - Java Runtime Environment 11.0.2
### - Python 3 Environment
### * Your Excellent Skills

## Setting Up Directories
1.Run Git Clone:
```bash
git clone https://github.com/BXYMartin/OO-Public-Test.git
```

2.Enter Directory:
```bash
cd OO-Public-Test
```

3.Setup Sub Directories:
```bash
cd test_path/
git clone https://github.com/BXYMartin/OO-Public.git tmp
mv tmp/.git .
rm -rf tmp
git reset --hard HEAD
```

4.Initialize Submodule:
```bash
git submodule init
git submodule update
```

5.Modify Path:
```bash
cd ..
nano start.sh # Change First Line to Your Path
```

> Now you're ready to go.

You may consult [OO-Public Readme](https://github.com/BXYMartin/OO-Public) to put your jar into the test system.

## Starting UML Autotest
### Manually Run
Setup Running Variables:
```bash
./start.sh x x # Run with Test Generation
./start.sh x   # Run with Stored Tests
./start.sh     # Run with Presets
```
### Automatic Test
Edit `test.cron` and try:
```bash
crontab test.cron
crontab -l
```

Default setup will automatically run once per hour.

## Relevant Info
The basic structure of this test is evolved from [Elevator Testing Service](https://github.com/BXYMartin/Java-Elevator/tree/test_multi), Path Testing Service(Not Published Yet) and [Poly Testing Service](https://github.com/BXYMartin/Java-Polynomial/tree/java_test). They are projects of my Object-Oriented Programming Course.

[OO-Public](https://github.com/BXYMartin/OO-Public) and [OO-Posts](https://github.com/Catherine9811/OO-Posts) are two sub projects included in this project, special thanks to github for providing this awesome platform.

## Bug Report
Please Contact BXYMartin@buaa.edu.cn
