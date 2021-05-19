# :umbrella: NYX

## :wrench: How to run local

1. Certify that you have installed in your machine
	- [Git](https://git-for-windows.github.io/)
	- [Python 3.8 >](https://www.python.org/)

2. In your CLI, use the following commands!
   
```bash
# Clone this repository
$ git clone https://github.com/has256/nyx

# Go into the repository
$ cd nyx

# Install dependencies
$ pip3 install -r requirements.txt 

# Install nyx
$ sudo python3 setup.py install

# Use nyx
$ nyx
```

## :checkered_flag: Usage

Now that you have Nyx installed, you can start using Nyx. Here are some of the most common commands you’ll need.

- Show all commands and help messages
```bash
nyx --help
```

- Open UFABC website
```bash
nyx site ufabc
```

- Return all current subjects (and empty/high-demand). Real-time monitoring.
```bash
nyx matriculas ofertadas --ingressantes
nyx matriculas vazias
nyx matriculas alta-demanda
nyx matriculas watch
```

- Return your subjects (and subjects info)
```bash
nyx matriculas minha-grade
nyx ementas "Bases Matemáticas"
```

- Retrieve some professors and students info's
```bash
nyx aluno info abreu.carlos
nyx professor "Bases Matemáticas"
nyx docente area-de-pesquisa "username"
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

