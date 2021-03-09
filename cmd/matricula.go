package cmd

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strconv"

	"github.com/spf13/cobra"
)

type Disciplina []struct {
	NomeCampus        string      `json:"nome_campus"`
	VagasIngressantes interface{} `json:"vagas_ingressantes"`
	Horarios          []struct {
		Horas                []string `json:"horas"`
		PeriodicidadeExtenso string   `json:"periodicidade_extenso"`
		Semana               int      `json:"semana"`
	} `json:"horarios"`
	Campus           int    `json:"campus"`
	Tpi              []int  `json:"tpi"`
	Creditos         int    `json:"creditos"`
	Codigo           string `json:"codigo"`
	Nome             string `json:"nome"`
	Obrigatoriedades []struct {
		Obrigatoriedade string `json:"obrigatoriedade"`
		CursoID         int    `json:"curso_id"`
	} `json:"obrigatoriedades"`
	Recomendacoes interface{} `json:"recomendacoes"`
	ID            int         `json:"id"`
	Vagas         int         `json:"vagas"`
}

var (
	vazia        bool
	ofertadas    bool
	altaDemanda  bool
	ingressantes bool
	matriculaCmd = &cobra.Command{ //need refactor
		Use:   "matricula",
		Short: "Utilitarios relativos a matricula",
		Run: func(cmd *cobra.Command, args []string) {

			res, _ := http.Get("https://matricula.ufabc.edu.br/cache/todasDisciplinas.js")
			body, _ := ioutil.ReadAll(res.Body)
			var todasDisciplinas Disciplina
			_ = json.Unmarshal([]byte(body[17:len(body)-2]), &todasDisciplinas)

			var contagem map[string]string

			resContagem, _ := http.Get("https://matricula.ufabc.edu.br/cache/contagemMatriculas.js")
			bodyContagem, _ := ioutil.ReadAll(resContagem.Body)
			_ = json.Unmarshal([]byte(bodyContagem[19:len(bodyContagem)-2]), &contagem)

			if vazia {
				for _, disciplina := range todasDisciplinas {
					req := contagem[strconv.Itoa(disciplina.ID)]
					requisicoes, _ := strconv.Atoi(req)
					// need to cover corner cases (ingressantes)
					if requisicoes < disciplina.Vagas {
						fmt.Printf("%s ainda tem vagas.\n", disciplina.Nome)
					}
				}
				os.Exit(0)
			}

			if altaDemanda {
				fmt.Println("Disciplinas em Alta Demanda")
				for _, disciplina := range todasDisciplinas {
					req := contagem[strconv.Itoa(disciplina.ID)]
					requisicoes, _ := strconv.Atoi(req)
					if requisicoes >= (15*disciplina.Vagas)/10 {
						fmt.Printf("%s\n", disciplina.Nome)
					}
				}
				os.Exit(0)
			}

			if ofertadas {
				for _, disciplina := range todasDisciplinas {
					if ingressantes {
						if disciplina.VagasIngressantes != nil {
							fmt.Printf("%s com %v vagas dedicadas.\n", disciplina.Nome, disciplina.VagasIngressantes)
							continue
						}
					} else {
						fmt.Printf("%s com %v vagas.\n", disciplina.Nome, disciplina.Vagas)
					}
				}
			} else {
				cmd.Help()
			}
		},
	}
)

func init() {
	type MyFlag struct {
		refVerbose  *bool
		verboseFlag string
		shortFlag   string
		hasFlag     bool
		description string
	}

	var myFlags []MyFlag
	myFlags = []MyFlag{
		{&ofertadas, "ofertadas", "o", false, "retorna os nomes/vagas das disciplinas ofertadas (consulta real-time ao sistema)"},
		{&ingressantes, "ingressantes", "i", false, "retorna disciplinas ofertadas de discentes ingressantes"},
		{&vazia, "vazia", "z", false, "retorna disciplinas com menos vagas que requisições"},
		{&altaDemanda, "alta-demanda", "a", false, "retorna disciplinas em alta demanda"},
	}

	for _, flag := range myFlags {
		matriculaCmd.Flags().BoolVarP(
			flag.refVerbose,
			flag.verboseFlag,
			flag.shortFlag,
			flag.hasFlag,
			flag.description,
		)
	}

	rootCmd.AddCommand(matriculaCmd)
}
