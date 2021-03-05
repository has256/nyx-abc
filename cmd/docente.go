package cmd

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"

	"github.com/spf13/cobra"
)

type docente struct {
	NomeCompleto string `json:"nome"`
	Siape        string `json:"siape"`
}

var (
	nome       bool
	siape      bool
	docenteCmd = &cobra.Command{
		Use:   "docente",
		Short: "Utilitários relacionados à docentes",
		Run: func(cmd *cobra.Command, args []string) {

			if len(args) == 0 {
				cmd.Help()
				os.Exit(-1)
			}
			res, _ := http.Get("https://sig.ufabc.edu.br/sigaa/APISistemasNTI?funcao=1&valor=" + args[0])
			body, _ := ioutil.ReadAll(res.Body)
			docente := docente{}
			jsonErr := json.Unmarshal(body, &docente)

			if jsonErr != nil {
				log.Fatal(jsonErr)
			}

			if info {
				fmt.Println(docente)
			} else if email {
				fmt.Println(args[0] + "@aluno.ufabc.edu.br")
			} else if usuario {
				fmt.Println(args[0])
			} else if nome {
				fmt.Println(docente.NomeCompleto)
			} else if siape {
				fmt.Println(docente.Siape)
			}

		},
	}
)

func init() {
	rootCmd.AddCommand(docenteCmd)
	docenteCmd.Flags().BoolVarP(
		&info, "info",
		"i", false, "retorna as informacoes de algum(a) docente",
	)
	docenteCmd.Flags().BoolVarP(
		&email, "email",
		"e", false, "retorna o e-mail de algum(a) docente",
	)
	docenteCmd.Flags().BoolVarP(
		&siape, "siape",
		"s", false, "retorna o SIAPE de algum(a) docente",
	)
	docenteCmd.Flags().BoolVarP(
		&nome, "nome-completo",
		"n", false, "retorna o nome completo de algum(a) docente",
	)
}