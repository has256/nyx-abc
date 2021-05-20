# :umbrella: NYX.ABC

## :computer: How to Install
   
```bash
$ pip3 install nyx-abc
```

## :checkered_flag: Usage

Now that you have nyx_abc installed, you can start using nyx_abc. Here are some of the most common commands you’ll need.

- Show all commands and help messages
```bash
nyx-abc --help
```

- Open UFABC website
```bash
nyx-abc site ufabc
```

- Return all current subjects (and empty/high-demand). Real-time monitoring.
```bash
nyx-abc matriculas ofertadas --ingressantes
nyx-abc matriculas vazias
nyx-abc matriculas alta-demanda
nyx-abc matriculas watch
```

- Return your subjects (and subjects info)
```bash
nyx-abc matriculas minha-grade
nyx-abc ementas "Bases Matemáticas"
```

- Retrieve some professors and students info's
```bash
nyx-abc aluno info abreu.carlos
nyx-abc docente area-de-pesquisa "username"
```

## :wrench: How to run local

1. Certify that you have installed in your machine
	- [Git](https://git-for-windows.github.io/)
	- [Python 3.8 >](https://www.python.org/)

2. In your CLI, use the following commands!
   
```bash
# Clone this repository
$ git clone https://github.com/has256/nyx_abc

# Go into the repository
$ cd nyx_abc

# Install dependencies
$ pip3 install -r requirements.txt 

# Install nyx_abc
$ sudo python3 setup.py install

# Use nyx_abc
$ nyx-abc
```

## :hearts: Contributing

For bug fixes, documentation improvements, typos, translations (new/updates) and simple changes, just make a PR! tada
For more complex changes, pls, make an issue first so we can discuss the design.

Roadmap for contributing:

1. Fork it.
2. Create your feature branch (git checkout -b my-new-feature).
3. Commit your changes (git commit -am 'Add some feature').
4. Push to the branch (git push origin my-new-feature).
5. Create new Pull Request.

## :page_facing_up: License

Everything here is licensed by MIT License.
