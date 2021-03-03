package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var (
	tidia   bool
	siteCmd = &cobra.Command{
		Use:   "site",
		Short: "Abre os horrorosos sites da UFABC",
		Run: func(cmd *cobra.Command, args []string) {
			if tidia {
				fmt.Println("site called")
				os.Exit(0)
			}
			if len(args) == 0 {
				cmd.Help()
			}
		},
	}
)

func init() {

	siteCmd.Flags().BoolVarP(
		&tidia, "tidia",
		"t", false, "abre o site do tidia",
	)

	rootCmd.AddCommand(siteCmd)
}
