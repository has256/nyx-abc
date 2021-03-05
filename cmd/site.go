package cmd

import (
	"log"
	"os"
	"os/exec"

	"github.com/spf13/cobra"
)

func openBrowser(url string) {
	var err error
	exec.Command("xdg-open", url).Start()
	if err != nil {
		log.Fatal(err)
	}
	os.Exit(0)
}

var (
	siteCmd = &cobra.Command{
		Use:   "site",
		Short: "Abre os horrorosos sites da UFABC",
		Run: func(cmd *cobra.Command, args []string) {
			if len(args) == 0 {
				cmd.Help()
				os.Exit(-1)
			}

			switch args[0] {
			case "tidia":
				openBrowser("https://tidia4.ufabc.edu.br/portal/relogin")
			case "prograd":
				openBrowser("https://prograd.ufabc.edu.br/")
			case "gradmat":
				openBrowser("https://gradmat.ufabc.edu.br/")
			case "bcc":
				openBrowser("https://bcc.ufabc.edu.br")
			case "sigaa":
				openBrowser("https://sig.ufabc.edu.br/sigaa/verTelaLogin.do")
			case "moodle":
				openBrowser("https://moodle.ufabc.edu.br/")
			case "neuro":
				openBrowser("https://neuro.ufabc.edu.br/")
			case "ufabc":
				openBrowser("https://www.ufabc.edu.br/")
			}

		},
	}
)

func init() {
	rootCmd.AddCommand(siteCmd)
}
