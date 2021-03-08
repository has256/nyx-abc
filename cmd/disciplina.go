package cmd

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"

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
	ofertadas     bool
	ingressantes  bool
	disciplinaCmd = &cobra.Command{
		Use:   "disciplina",
		Short: "Utilitarios relativos a disciplinas",
		Run: func(cmd *cobra.Command, args []string) {

			res, _ := http.Get("https://matricula.ufabc.edu.br/cache/todasDisciplinas.js")
			body, _ := ioutil.ReadAll(res.Body)
			var todasDisciplinas Disciplina
			_ = json.Unmarshal([]byte(body[17:len(body)-2]), &todasDisciplinas)

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
	}

	for _, flag := range myFlags {
		disciplinaCmd.Flags().BoolVarP(
			flag.refVerbose,
			flag.verboseFlag,
			flag.shortFlag,
			flag.hasFlag,
			flag.description,
		)
	}

	rootCmd.AddCommand(disciplinaCmd)
}
